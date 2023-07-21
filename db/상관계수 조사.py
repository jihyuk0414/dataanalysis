import pymysql
import numpy as np 

# 변수 선언 입니다.
conn, cur = None, None
nogji = []
nogji1 = []
traffic = []
culture=[]
business = []
medical = []
house = []
economy = []
satisfiy = []
row = None

# 디비와 파이썬간의 연결을 나타낸 코드입니다.
conn = pymysql.connect(host='172.30.1.53', user='jihyuk', password='asas1212', db='dataanalysis', charset='utf8')
cur = conn.cursor()

cur.execute(" SELECT 전체녹지 FROM 녹지면적 WHERE 소재지 = '동작구' and 년도 between 2010 and 2021 ")

while True:
    row = cur.fetchone()
    if row is None:
        break
    nogji.append(row[0])

cur.execute("select `1인당 녹지` from 인당녹지 where 소재지 = '동작구' and 년도 between 2010 and 2021")

while True:
    row = cur.fetchone()
    if row is None:
        break
    nogji1.append(row[0])

cur.execute(" select 대중교통만족도 from 교통 where 소재지 = '동작구' and 년도 between 2010 and 2021 ")

while True:
    row = cur.fetchone()
    if row is None:
        break
    traffic.append(row[0])

cur.execute(" select 총합 from 문화시설수 WHERE 소재지 = '동작구' and 년도 between 2010 and 2021 ")

while True:
    row = cur.fetchone()
    if row is None:
        break
    culture.append(row[0])    

cur.execute(" select 용도지역현황 from 상업지역 WHERE 소재지 = '동작구' and 년도 between 2010 and 2021 ")

while True:
    row = cur.fetchone()
    if row is None:
        break
    business.append(float(row[0].replace(',', '')))
    
cur.execute("select `병원 수` from 의료시설 WHERE 소재지 = '동작구' and 년도 between 2010 and 2021 ")

while True:
    row = cur.fetchone()
    if row is None:
        break
    medical.append(row[0])

cur.execute("select `안정화지수` from 주택 WHERE 소재지 = '동작구' and 년도 between 2010 and 2021 ")

while True:
    row = cur.fetchone()
    if row is None:
        break
    house.append(row[0])
    
cur.execute("select `지역내총생산(2015년 기준/ 연쇄가격) (백만원)` from 경제수준 where 소재지 = '동작구' and 년도 between 2010 and 2021 ")

while True:
    row = cur.fetchone()
    if row is None:
        break
    economy.append(row[0])   

cur.execute("select 주거환경만족도 from 주거환경만족도 where 소재지 = '동작구' and 년도 between 2010 and 2021 ; ")

while True:
    row = cur.fetchone()
    if row is None:
        break
    satisfiy.append(row[0]) 




conn.close()

# 결과 출력
print("전체녹지:")
for data in nogji:
    print("%8s" % data)

print("1인당녹지:")
for data in nogji1:
    print("%8s" % data)

print("대중교통만족도:")
for data in traffic:
    print("%8s" % data)
    
print("문화 총합:")
for data in culture:
    print("%8s" % data)

print("용도지역현황:")
for data in business:
    print("%8s" % data)

print("병원 수:")
for data in medical:
    print("%8s" % data)

    
print("주택 안정화 지수:")
for data in house:
    print("%8s" % data)

print("경제수준:")
for data in economy:
    print("%8s" % data)

print("주거 환경 만족도:")
for data in satisfiy:
    print("%8s" % data)



#상관관계3개 함수

# 상관관계 top 3 뽑기
def find_top3_variables(nogji, nogji1, traffic, culture, business, medical, house, satisfiy):
    variables = {
        'nogji': np.abs(np.corrcoef(nogji, satisfiy)[0, 1]),
        'nogji1': np.abs(np.corrcoef(nogji1, satisfiy)[0, 1]),
        'traffic': np.abs(np.corrcoef(traffic, satisfiy[:11])[0, 1]),
        'culture': np.abs(np.corrcoef(culture, satisfiy)[0, 1]),
        'business': np.abs(np.corrcoef(business, satisfiy)[0, 1]),
        'medical': np.abs(np.corrcoef(medical, satisfiy)[0, 1]),
        'house': np.abs(np.corrcoef(house, satisfiy)[0, 1]),
        'economy': np.abs(np.corrcoef(economy, satisfiy[:11])[0, 1])
    }
    for variable, correlation in variables.items():
        print(f"{correlation}")
    top3_variables = sorted(variables, key=variables.get, reverse=True)[:3]

    
    return top3_variables

# 상위 3개 변수 찾기
top3_variable_names = find_top3_variables(nogji, nogji1, traffic, culture, business, medical, house, satisfiy)

print("상위 3개 변수:", top3_variable_names)


