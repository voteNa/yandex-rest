class StatsRepo:
    def getBirthday(self, import_id: int):
        from app import db
        result = db.session().execute('''
        with presents as (
            select json_build_object('citizen_id', cc.citizen_id,
                                     'presents', count(*)) ar,
                   extract(month from cr.birth_date)       mon
            from citizen cc
                     left join citizen cr on (cr.citizen_id in (select unnest(cc.relatives)))
            where cc.import_id = :import_id and cr.import_id = :import_id
            group by mon, cc.citizen_id
        )
        select json_agg(presents.ar) dictr, mon
        from presents
        group by presents.mon

        ''', {'import_id': import_id})
        from src.models.birthday_stat import BirthdayStat
        birthday_stat = BirthdayStat()
        for monthValue in result:
            birthday_stat.setMonth(month=(monthValue['mon']), value=(monthValue['dictr']))

        return birthday_stat

    def getPercentile(self, import_id: int):
        from app import db
        from src.models.percentile_stat import PercentileStat
        result = db.session().execute('''
        select
            town,
            percentile_cont(0.5) within group (order by extract(YEARS from age(birth_date))) as p50,
            percentile_cont(0.75) within group (order by extract(YEARS from age(birth_date))) as p75,
            percentile_cont(0.99) within group (order by extract(YEARS from age(birth_date))) as p99
        from citizen
        where import_id = :import_id        
        group by town
        ''', {'import_id': import_id})
        percentile_stat = PercentileStat()
        for value in result:
            percentile = {
                'town': value['town'],
                'p50': value['p50'],
                'p75': value['p75'],
                'p99': value['p99']
            }
            percentile_stat.setPercentile(percentile=percentile)

        return percentile_stat



