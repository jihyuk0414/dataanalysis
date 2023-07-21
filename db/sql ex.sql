CREATE TABLE mytable (
  id INT PRIMARY KEY,
  myname VARCHAR(20)
);

create table forpractable(
rid int primary key , 
eid int ,
sid char 
show tables;

select * from example;

select * from prac6;

show tables;

select * from longexample;

select RESPOND_ID from longexample where SEXDSTN_FLAG_CD = 'F' ;

show databases;

SELECT user, authentication_string, plugin FROM mysql.user;

create schema projectschema ; 

show tables;

select * from 녹지면적 natural join 인당녹지;

select 소재지 from 녹지면적 where 완충녹지< 50000 and 년도 = 2007;

select `1인당 녹지` from 녹지면적 natural join 인당녹지
where 소재지 = '중랑구';

create table fcktable(
pid char);

insert into fcktable values('');

select * from 주택;


select * from 인당녹지;

ALTER TABLE `자치구별+지역내총생산(2015년+기준)-정렬완료` RENAME TO `경제수준`;

SELECT distinct 교통.대중교통만족도
FROM 교통
NATURAL JOIN 상업지역
WHERE 상업지역.용도지역현황 = (
  SELECT MAX(용도지역현황)
  FROM 상업지역
) and 년도 = 2020;


select 주거환경만족도 from 주거환경만족도 where 소재지 = '중랑구'  and 년도 between 2010 and 2021 ;

select 대중교통만족도 from 교통 where 소재지 = '종로구' and 년도 between 2010 and 2021 ;

show tables;

select `1인당 녹지` from 인당녹지 where 소재지 = '종로구' and 년도 between 2010 and 2021;

select `지역내총생산(2015년 기준/ 연쇄가격) (백만원)` from 경제수준 where 소재지 = '종로구' and 년도 between 2010 and 2021;

select 	대중교통만족도 from 교통 where 소재지 = '종로구' and 년도 between 2010 and 2021;


SELECT 전체녹지 FROM 녹지면적 WHERE 소재지 = '종로구' and 년도 between 2010 and 2021; 

select 총합 from 문화시설수 WHERE 소재지 = '종로구' and 년도 between 2010 and 2021;

select 용도지역현황 from 상업지역 WHERE 소재지 = '종로구' and 년도 between 2010 and 2021;



select `안정화지수` from 주택 WHERE 소재지 = '종로구' and 년도 between 2010 and 2021;

select distinct 소재지 from 주거환경만족도;

select * from 의료시설 order by 소재지;

select * from 주택;


select `병원 수` from 의료시설 NATURAL JOIN 상업지역 WHERE 소재지 = '서초구' and 년도 between 2010 and 2021;

select 소재지,avg(`병원 수`), max(`용도지역현황`) from 의료시설 NATURAL JOIN 상업지역 group by 소재지 ;


select * from 상업지역;