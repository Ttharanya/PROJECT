
import sys #provide access to system-specific parameters and functions
import csv

def add(i):
    with open('record.csv','a+',newline='')as file:
        writer=csv.writer(file)
        writer.writerow(i)


def view():
    data=[]
    with open('record.csv') as file:
        reader=csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data

#view()

def remove(i):
    def save(j): #to update the list after removal
        with open('record.csv','w',newline='')as file:
            writer=csv.writer(file)
            writer.writerows(j)
    new_list=[]
    telephone=i

    with open('record.csv','r')as file:
        reader=csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                if element==telephone:
                    new_list.remove(row)
    save(new_list)

#remove('2345')
#view()

def update(i):
    def update_newlist(j):
        with open('record.csv','w',newline='')as file:
            writer=csv.writer(file)
            writer.writerows(j)
    new_list=[]
    telephone=i[0]
    ['123','demo','M','123','demo2@gmail.com']
    with open('record.csv','r')as file:
        reader=csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element ==telephone:
                    name=i[1]
                    gender=i[2]
                    telephone=i[3]
                    email=i[4]
                    data=[name,gender,telephone,email]
                    index=new_list.index(row)
                    new_list[index]=data
    update_newlist(new_list)
#sample=['123','girlcoder','F','123','girl12@gmail.com']
#update(sample)

def search(i):
    data=[]
    telephone=i
    with open('record.csv','r')as file:
        reader=csv.reader(file)
        for row in reader:
            for element in row:
                if element==telephone:
                    data.append(row)
    print(data)
    return data
search('123')