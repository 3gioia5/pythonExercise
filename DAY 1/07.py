# 투표 집계하기

votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

vote_counter = {}

for name in votes:
    if name not in vote_counter:
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1

print(vote_counter)