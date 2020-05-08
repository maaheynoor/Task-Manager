from tkinter import *
from datetime import datetime
# import our class and functions

from assistantSpeak import assistant_speaks
from getAudio import get_audio
from getDateTime import *


class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        # speak icon image
        self.mikeTodo = PhotoImage(file='images\mike5.png')
        self.speakicon = self.mikeTodo.subsample(25, 20)

        # task manager
        self.task = StringVar()
        self.date = StringVar()
        self.time = StringVar()
        self.taskFrame = Frame(self, width=300, height=100)
        self.taskFrame.grid(row=0,column=0,ipadx=10, pady=20, sticky='news')
        self.taskheading = Label(self.taskFrame,text='Task', font=('Verdana',12, 'bold'), bg="peachpuff", fg="deeppink4")
        self.taskheading.grid(row=0, column=0, columnspan=3,pady=3)
        self.labelTask = Label(self.taskFrame, text='Task',font=('calibri',10),fg='black')
        self.labelTask.grid(row=1, column=0,pady=3)
        self.inputTask = Entry(self.taskFrame,textvariable=self.task)
        self.inputTask.grid(row=1, column=1,pady=3)
        self.labelDate = Label(self.taskFrame, text='Date',font=('calibri',10),fg='black')
        self.labelDate.grid(row=2, column=0,pady=3)
        self.inputDate = Entry(self.taskFrame,textvariable=self.date)
        self.inputDate.grid(row=2, column=1,pady=3)
        self.labelTime = Label(self.taskFrame, text='Time',font=('calibri',10),fg='black')
        self.labelTime.grid(row=3, column=0,pady=3)
        self.inputTime = Entry(self.taskFrame,textvariable=self.time)
        self.inputTime.grid(row=3, column=1,pady=3)
        self.s = Button(self.taskFrame,image=self.speakicon,height=50,command=lambda: self.actionSpeakTask())
        self.s.image = self.speakicon
        self.s.grid(row=1, column=2, rowspan=4,padx=5,ipadx=3)

        self.addTask = Button(self.taskFrame, text="Add",  fg="peachpuff", bg="hotpink4",font=('Verdana',11),
                              command=lambda: self.actionAddTask())
        self.addTask.grid(row=6, column=0,columnspan=2)


        # todomanager
        self.todoFrame = Frame(self, width=300, height=100)
        self.todoFrame.grid(row=1,column=0, ipadx=10, pady=20, sticky='news')
        self.todoheading = Label(self.todoFrame, text='ToDo', font=('Verdana', 12, 'bold'), bg="peachpuff",
                                 fg="deeppink4")
        self.todoheading.grid(row=0, column=0, columnspan=3,pady=3)
        self.labelTodo = Label(self.todoFrame, text='Todo',font=('calibri', 10), fg='black')
        self.labelTodo.grid(row=1, column=0,pady=3)
        self.inputTodo = Entry(self.todoFrame)
        self.inputTodo.grid(row=1, column=1,pady=3)

        self.s = Button(self.todoFrame, image=self.speakicon, compound=LEFT,
                        command=lambda: self.actionSpeakTask())
        self.s.image = self.speakicon
        self.s.grid(row=1, column=2, padx=5, ipadx=3)

        self.addTodo = Button(self.todoFrame, text="Add", fg="peachpuff", bg="hotpink4",font=('Verdana',11),
                              command=lambda: self.actionAddTodo())
        self.addTodo.grid(row=3, column=0,columnspan=2)

        # note manager
        self.noteFrame = Frame(self, width=300, height=100)
        self.noteFrame.grid(row=2,column=0,ipadx=10, pady=20, sticky='news')
        self.noteheading = Label(self.noteFrame, text='Note', font=('Verdana', 12, 'bold'), bg="peachpuff",
                                 fg="deeppink4")
        self.noteheading.grid(row=0, column=0, columnspan=3,pady=3)
        self.labelTitle = Label(self.noteFrame, text='Title', font=('calibri', 10), fg='black')
        self.labelTitle.grid(row=1, column=0,pady=3)
        self.inputTitle = Entry(self.noteFrame, textvariable=self.task)
        self.inputTitle.grid(row=1, column=1,pady=3)
        self.s = Button(self.noteFrame, image=self.speakicon, compound=LEFT,
                        command=lambda: self.actionSpeakNoteTitle())
        self.s.image = self.speakicon
        self.s.grid(row=1, column=2, padx=5, ipadx=3)
        self.labelNote = Label(self.noteFrame, text='Note',font=('calibri', 10), fg='black')
        self.labelNote.grid(row=2, column=0,pady=3)
        self.inputNote =Text(self.noteFrame,height=5,width=20)
        self.inputNote.grid(row=2, column=1,pady=3)
        self.s = Button(self.noteFrame, image=self.speakicon, compound=LEFT,
                        command=lambda: self.actionSpeakNote())
        self.s.image = self.speakicon
        self.s.grid(row=2, column=2, padx=5, ipadx=3)

        self.addNote = Button(self.noteFrame, text="Add",  fg="peachpuff", bg="hotpink4",font=('Verdana',11),
                              command=lambda: self.actionAddNote())
        self.addNote.grid(row=4, column=0,columnspan=2)

        # schedule and help frame in the bottom
        """ master is frame containing contents
        master.master is canvas
        master.master.master is frame containing canvas used for switching between pages"""
        self.topButtonFrame = Frame(self, width=300, height=300)
        self.topButtonFrame.grid(row=3,column=0,ipadx=10, pady=20)
        schedule = Button(self.topButtonFrame, text="Schedule",
                          fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
                          command=lambda: self.master.master.master.switch_frame(SchedulePage))
        schedule.pack(pady=5)
        help = Button(self.topButtonFrame, text="Help",
                      fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
                      command=lambda: self.master.master.master.switch_frame(HelpPage))
        help.pack()

    def actionSpeakTask(self):
        assistant_speaks('How can I help you ?')
        self.inputTask.delete(0, END)
        self.inputDate.delete(0, END)
        self.inputTime.delete(0, END)
        assistant_speaks("Please specify the task to be performed")
        text = get_audio()
        self.task.set(text)
        assistant_speaks("Please specify the day")
        text = get_audio()
        tdate = DateFromText(text)  # get time from date
        self.date.set(tdate)
        assistant_speaks("Please mention the time")
        text = get_audio()
        time = TimeFromText(text)  # get time from text
        self.time.set(time)


    def actionAddTask(self):
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            task=self.inputTask.get()
            print(task)
            date = self.inputDate.get()
            print(date)
            time = self.inputTime.get()
            print(time)
            str = "INSERT INTO task(task,date,time) VALUES ('" + task + "','" + date + "','"+time+"');"
            cursor.execute(str)
            connection.commit()
            assistant_speaks("Task added successfully")
            self.inputTask.delete(0, END)
            self.inputDate.delete(0, END)
            self.inputTime.delete(0, END)
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()

    def actionSpeakTodo(self):
        assistant_speaks('Please specify the tile ')
        self.inputTodo.delete(0, END)
        voice = get_audio()
        voice = voice.lower()
        print(voice)

    def actionAddTodo(self):
        pass

    def actionSpeakNoteTitle(self):
        assistant_speaks('How can I help you ?')
        self.inputTitle.delete(0, END)
        voice = get_audio()
        voice = voice.lower()
        print(voice)

    def actionSpeakNote(self):
        assistant_speaks('How can I help you ?')
        voice = get_audio()
        voice = voice.lower()
        print(voice)

    def actionAddNote(self):

        self.inputTitle.delete(0, END)
        self.inputNote.delete(0, END)



class SchedulePage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.displayTaskButton = Button(self, text="Display Tasks",
                                        fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
                                        command=lambda: master.master.master.switch_frame(DisplayTaskPage))
        self.displayTaskButton.grid(row=0, column=0,pady=5)
        self.displayTodoButton = Button(self, text="Display ToDo",
                                        fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
                                        command=lambda: master.master.master.switch_frame(DisplayTaskPage))
        self.displayTodoButton.grid(row=2, column=0,pady=5)
        self.displayNoteButton = Button(self, text="Display Notes",
                                        fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
                                        command=lambda: master.master.master.switch_frame(DisplayNotePage))
        self.displayNoteButton.grid(row=4, column=0,pady=5)
        self.back = Button(self, text="Back",
                           fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
                           command=lambda: master.master.master.switch_frame(StartPage))
        self.back.grid(row=6, column=0,pady=5)


# Display task page
class DisplayTaskPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #backimage = PhotoImage(file="images\\back3.png")
        #backicon = backimage.subsample(10, 10)
        self.display = Label(self, text="Display Tasks for which of the following:",font=("calibri",12, "bold"))
        self.display.grid(row=0, column=0,columnspan=5)
        self.font=("calibri","11")
        self.radiovar = StringVar()
        # Option for specific day, btw two days, upcoming tasks or all task in the db
        self.R1 = Radiobutton(self, text="Specific Day",variable=self.radiovar, value="Specific Day", tristatevalue="x",
                              font=self.font,command=self.displayTask)
        self.R1.grid(row=1, column=0,columnspan=2)
        self.R2 = Radiobutton(self, text="Between two days", variable=self.radiovar, value="Between two days", tristatevalue="x",
                              font=self.font,command=self.displayTask)
        self.R2.grid(row=1, column=2,columnspan=3)
        self.R3 = Radiobutton(self, text="All Upcoming", variable=self.radiovar, value="All Upcoming", tristatevalue="x",
                              font=self.font,command=self.displayTask)
        self.R3.grid(row=2, column=0,columnspan=2)
        self.R4 = Radiobutton(self, text="All", variable=self.radiovar, value="All",tristatevalue="x",
                              font=self.font,command=self.displayTask)
        self.R4.grid(row=2, column=1,columnspan=3)
        self.back = Button(self, text="Back", fg="peachpuff", bg="hotpink4", font=('Verdana', 10, 'bold'),
                           command=lambda: master.master.master.switch_frame(SchedulePage))
        # self.back.image=backicon
        self.back.grid(row=3, column=0, columnspan=5)
        self.displayTask = Label(self,font=("Verdana", "12", "bold"))
        self.displayTask.grid(row=4,column=0,columnspan=5,pady=8)


    def displayTask(self):

        selection = self.radiovar.get()
        input = False
        # For specific Day only one speech input is taken
        if selection == "Specific Day":
            assistant_speaks("Please mention the day")
            date=get_audio()
            date = DateFromText(date)
            if date==None:
                input=False
            else:
                input= True
        # Two days taken as input (start and end date)
        elif selection=="Between two days":
            assistant_speaks("Please mention the start date")
            sdate = get_audio()
            sdate=DateFromText(sdate)
            assistant_speaks("Please mention the end date")
            edate = get_audio()
            edate = DateFromText(edate)
            if sdate==None or edate==None:
                input=False
            else:
                input= True
        # No speech input for all upcoming or all tasks
        elif selection=="All Upcoming":
            today = datetime.date.today()
            input=True
        elif selection=="All":
            input=True

        # If speech input is identified and there are dates/days present in them
        if input==True:

            try:
                connection = psycopg2.connect(user="usertm",
                                              password="password",
                                              host="127.0.0.1",
                                              port="5432",
                                              database="TaskManager")
                cursor = connection.cursor()
                if selection == "Specific Day":
                    date = date.strftime("%Y-%m-%d")
                    print("Date:", date)
                    query = "SELECT * FROM task WHERE date='"+date+"' ORDER BY time;"
                    selection= selection+" : "+date
                elif selection=="Between two days":
                    sdate = sdate.strftime("%Y-%m-%d")
                    edate = edate.strftime("%Y-%m-%d")
                    print("Start Date:",sdate," End date:",edate)
                    query = "SELECT * FROM task WHERE date>='" + sdate + "' AND date<='"+edate+"' ORDER BY date,time;"
                    selection = " Between " + sdate+" and "+edate
                elif selection=="All Upcoming":
                    today = today.strftime("%Y-%m-%d")
                    query = "SELECT * FROM task WHERE date>='" + today + "' ORDER BY date,time;"
                    selection = "All Upcoming Tasks"
                elif selection == "All":
                    query = "SELECT * FROM task ORDER BY date,time;"
                    selection="All Tasks"
                cursor.execute(query)
                self.displayTask.config(text=selection)
                tasks=cursor.fetchall()
                # the data from db is display in grid with row>=5
                # First erase previous data
                for label in self.grid_slaves():
                    if int(label.grid_info()["row"]) >= 5:
                        label.grid_forget()
                index=5
                if len(tasks)>0:
                    stringtask="Task-Id\t\tTask\t\tDate\t\tTime\n"
                    Label(self, text="Task",font=("Artefact","12","bold")).grid(row=index, column=0)
                    Label(self, text="Date",font=("Artefact","12","bold")).grid(row=index, column=1)
                    Label(self, text="Time",font=("Artefact","12","bold")).grid(row=index, column=2)

                    dimage= PhotoImage(file='images\delete.png')
                    deleteicon = dimage.subsample(10, 10)
                    eimage= PhotoImage(file='images\edit.png')
                    editicon = eimage.subsample(10, 10)
                    # each task is displayed in a row and a delete button is associated with it
                    for task in tasks:
                        index = index + 1
                        Label(self, text=task[1],font=self.font,padx=5,pady=5).grid(row=index, column=0)
                        Label(self, text=str(task[2]),font=self.font,padx=5,pady=5).grid(row=index, column=1)
                        Label(self, text=str(task[3]),font=self.font,padx=5,pady=5).grid(row=index , column=2)
                        d=Button(self,text="Delete",image=deleteicon,
                                 command=lambda id=task[0],row=index: self.deleteTask(id,row,index+1))
                        d.image = deleteicon
                        d.grid(row=index, column=3)
                        e = Button(self, text="Edit", image=editicon,
                                   command=lambda id=task[0], row=index: self.displayEdit(id,row,index+1))
                        e.image = editicon
                        e.grid(row=index, column=4)
                        stringtask +=str(task[0])+"\t\t"+task[1]+"\t\t"+str(task[2])+"\t\t"+str(task[3])+"\n"
                    print(stringtask)
                    assistant_speaks("The Schedule is displayed")
                else:
                    assistant_speaks("There are no tasks")
                connection.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                connection.rollback()
                print("Error while using PostgreSQL table", error)
            finally:
                # closing database connection.
                if (connection):
                    cursor.close()
                    connection.close()
        # If no day is recognized or speech is not identified then user can try again
        else:
            assistant_speaks("Please repeat the process. Couldn't identify your audio or date mentioned")

        # update width and height of the canvas self is frame which is binded to canvas.. so self.master is canvas
        self.master.update()
        self.master.configure(scrollregion=self.master.bbox("all"))


    def deleteTask(self,id,row,index):
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            query="DELETE FROM task WHERE task_id="+str(id)+";"
            cursor.execute(query)
            for gridrow in self.grid_slaves():
                if int(gridrow.grid_info()["row"]) >= index:
                    gridrow.grid_forget()
            for label in self.grid_slaves():
                if int(label.grid_info()["row"])==row:
                    label.grid_forget()
            assistant_speaks("Deletion Successful")
            connection.commit()
        except (Exception , psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
        # closing database connection.
            if (connection):
                cursor.close()
                connection.close()

        # update width and height of the canvas self is frame which is binded to canvas.. so self.master is canvas
        self.master.update()
        self.master.configure(scrollregion=self.master.bbox("all"))

    def displayEdit(self,id,row,index):
        i=index
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            query="SELECT * FROM task WHERE task_id="+str(id)+";"
            cursor.execute(query)
            task = cursor.fetchone()
            Label(self, text="").grid(row=i, column=0, columnspan=5)
            i+=1
            ntask = StringVar(value=task[1])
            ndate = StringVar(value=task[2])
            ntime = StringVar(value=task[3])
            Label(self, text="Task:",font=("Lucida Bright", "10", "bold")).grid(row=i, column=0,columnspan=2)
            self.inputTask=Entry(self,textvariable=ntask)
            self.inputTask.grid(row=i,column=2,columnspan=2)
            i+=1
            Label(self, text="Date:",font=("Lucida Bright", "10", "bold")).grid(row=i, column=0, columnspan=2)
            self.inputDate=Entry(self, textvariable=ndate)
            self.inputDate.grid(row=i, column=2, columnspan=2)
            i += 1
            Label(self, text="Time:",font=("Lucida Bright", "10", "bold")).grid(row=i, column=0, columnspan=2)
            self.inputTime=Entry(self, textvariable=ntime)
            self.inputTime.grid(row=i, column=2, columnspan=2)
            i += 1
            mike = PhotoImage(file='images\mike5.png')
            mike = mike.subsample(13, 15)
            mikeButton = Button(self, image=mike,
                                command=lambda: self.speakTask())
            mikeButton.image = mike
            mikeButton.grid(row=i, column=1)

            simage = PhotoImage(file='images\save_edit.png')
            saveicon = simage.subsample(10, 10)
            s = Button(self, text="Save Changes",font=("Lucida Bright", "10", "bold"), image=saveicon, compound=LEFT,
                       command=lambda : self.editTask(id, row, index))
            s.image = saveicon
            s.grid(row=i, column=2, columnspan=3)
            assistant_speaks("Task details are displayed for editing")
            connection.commit()
        except (Exception , psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
        # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
        # update width of the canvas self is frame which is binded to canvas.. so self.master is canvas
        self.master.update()
        self.master.configure(scrollregion=self.master.bbox("all"))

    def speakTask(self):
        assistant_speaks("Is there any change in task?")
        text = get_audio()
        text=text.lower()
        if text.count("yes")>0:
            assistant_speaks("Please specify the task")
            text = get_audio()
            self.task.set(text)
        assistant_speaks("Is there any change in date?")
        text = get_audio()
        text = text.lower()
        if text.count("yes") > 0:
            assistant_speaks("Please specify the day")
            text = get_audio()
            tdate = DateFromText(text)  # get time from date
            self.date.set(tdate)
        assistant_speaks("Is there any change in time?")
        text = get_audio()
        text = text.lower()
        if text.count("yes") > 0:
            assistant_speaks("Please specify the time")
            text = get_audio()
            time = TimeFromText(text)  # get time from text
            self.time.set(time)


    def editTask(self,id,row,index):
        try:
            connection = psycopg2.connect(user="usertm",
                                          password="password",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="TaskManager")
            cursor = connection.cursor()
            cursor = connection.cursor()
            task = self.inputTask.get()
            print(task)
            date = self.inputDate.get()
            print(date)
            time = self.inputTime.get()
            print(time)
            query = "UPDATE task SET task='" + task + "',date='" + date + "',time='" + time + "' WHERE task_id="+str(id)+";"
            cursor.execute(query)
            for gridrow in self.grid_slaves():
                if int(gridrow.grid_info()["row"])>=index:
                    gridrow.grid_forget()
            Label(self, text=task).grid(row=row, column=0)
            Label(self, text=date).grid(row=row, column=1)
            Label(self, text=time).grid(row=row, column=2)
            assistant_speaks("Task edited successfully")
            connection.commit()
        except (Exception , psycopg2.DatabaseError) as error:
            connection.rollback()
            print("Error while using PostgreSQL table", error)
        finally:
        # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
        # update width of the canvas self is frame which is binded to canvas.. so self.master is canvas
        self.master.update()
        self.master.configure(scrollregion=self.master.bbox("all"))

class DisplayNotePage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.back = Button(self, text="Back",
                           fg="peachpuff", bg="hotpink4",
                           font=('Verdana', 10, 'bold'),
                           command=lambda: master.switch_frame(SchedulePage))
        self.back.grid(row=0, column=0)


class HelpPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.back = Button(self, text="Back",
                           fg="white", bg="DeepPink2",
                           command=lambda: master.switch_frame(SchedulePage))
        self.back.grid(row=0, column=0)
