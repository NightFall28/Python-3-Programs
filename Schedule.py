# Alice and Bob must schedule a meeting, given their schedules and working time, find the free times that they can meet each other.

AliceMeetings = [['08:00', '09:30'], ['09:30', '11:00'], ['13:00', '14:00'], ['15:00', '16:30']]
AliceWorkHours = ['07:00', '19:00']

BobMeetings = [['09:00', '10:30'], ['11:00', '12:00'], ['13:00', '14:30'], ['15:30', '17:00']]
BobWorkHours = ['07:00', '18:00']

def schedule_meeting(list1,list2,hours1,hours2):
    result = []

    if(hours1[0] < list1[0][0] and hours1[0] < list2[0][0] and hours1[0] >= hours2[0] and list1[0][0] <= list2[0][0]):
        result.append([hours1[0], list1[0][0]])
    elif(hours2[0] < list2[0][0] and hours2[0] < list1[0][0] and hours2[0] >= hours1[0] and list2[0][0] <= list1[0][0]):
        result.append([hours2[0], list2[0][0]])

    for i in range(1,len(list1)):
        list1_end = list1[i-1][1]
        list1_start = list1[i][0]
        j = i
        while(j < len(list2)):
            list2_end = list2[j-1][1]
            list2_start = list2[j][0]
            if(list2_end < list1_start):
                result.append([list2_end,list1_start])
            j += 1


    if(hours1[1] > list1[3][1] and hours1[1] > list2[3][1] and hours1[1] <= hours2[1] and list1[3][1] >= list2[3][1]):
        result.append([list1[3][1], hours1[1]])
    elif(hours2[1] > list2[3][1] and hours2[1] > list1[3][1] and hours2[1] <= hours1[1] and list2[3][1] >= list1[3][1]):
        result.append([list2[3][1],hours2[1]])

    return result

print("Meetings Can Be Scheduled During:",schedule_meeting(AliceMeetings,BobMeetings,AliceWorkHours,BobWorkHours))
