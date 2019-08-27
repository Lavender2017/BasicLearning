
sql = """

select *
from ibu_data_tech.channel_ratio
where to_date(create_time)>='$time1' and to_date(create_time)<='$time2'

"""