from string import Template
from template import sql_template


parm = {
    'time1':"2019-08-20",
    'time2':"2019-08-25"
}
sql = Template(sql_template.sql).substitute(parm)


print(sql)