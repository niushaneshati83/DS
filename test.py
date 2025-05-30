T=input()
for x in range(int(T)):
    nuisha = ''
    s=input()
    hour=s.split(":")
    time_meet=hour[1].split(" ")
    time_meet.insert(0,hour[0])
    if time_meet[2]=="PM" and int(time_meet[0])!=12:
        time_meet[0]=int(time_meet[0])+12
    if int(time_meet[0])==12 and time_meet[2]=="AM":
            time_meet[0]=0
    N=input()
    for y in range(int(N)):
        s=input()
        hour=s.split(" ")
        start_time=hour[0].split(":")
        start_time.append(hour[1])
        end_time=hour[2].split(":")
        end_time.append(hour[3])
        if start_time[2]=="PM" and int(start_time[0])!=12:
            start_time[0]=int(start_time[0])+12
        if int(start_time[0])==12 and start_time[2]=="AM":
            start_time[0]=0
        if end_time[2]=="PM" and int(end_time[0])!=12:
            end_time[0]=int(end_time[0])+12
        if int(end_time[0])==12 and end_time[2]=="AM":
            end_time[0]=0
        s_t=int(start_time[0])*60+int(start_time[1])
        e_t=int(end_time[0])*60+int(end_time[1])
        t_m=int(time_meet[0])*60+int(time_meet[1])
        if s_t <= t_m <= e_t:
            nuisha += '1'
        else:
            nuisha += '0'
    print(nuisha)
