/*
Object Name: show_cache
Object Type: DML
Purpose:
Shows the currently valid cache objects.

ChangeLog:
    Date    |    Author    |      Modification
    2021-01-26    |  stephen  |    Initial Definition
*/

select
    *
from
    youtube_query
where
    datediff(day, created_at, getdate()) < 90