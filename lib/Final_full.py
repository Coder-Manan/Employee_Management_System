import mysql.connector as s
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
db=s.connect(host='localhost',user='root',database='employee',passwd='12345678')
mc=db.cursor()
win1=tk.Tk()
win1.geometry()
win1.title('Welcome')
winopen=fopen=background=0
ba1,ba2,ba3,ba4,ba5,ba6,exa=0,0,0,0,0,0,0
un=0
name1=0
name2=0
img=tk.PhotoImage(file="Artboard-1@4x-8.png")
background=tk.Label(win1,image=img,bd=-7)
background.grid(row=0,column=0,rowspan=6,columnspan=2)
msg=tk.Label(win1,text='Management solutions')
msg.grid(row=0,column=0,columnspan=2)
msg.config(font=('phosphate',27))

l1=tk.Label(win1,text='Empid')
l1.grid(row=1,column=0,sticky='e')
l1.config(width='8',font=('silom',20))
i1=tk.Entry(win1)
i1.grid(row=1,column=1,sticky='w',padx='15')
l2=tk.Label(win1,text='Password')
l2.grid(row=2,column=0,sticky='e')
l2.config(width='8',font=('silom',20))
i2=tk.Entry(win1)
i2.grid(row=2,column=1,sticky='w',padx='15')

l3=tk.Label(win1,text='Passkey')
l3.grid(row=3,column=0,sticky='e')
l3.config(width='8',font=('silom',20))
i3=tk.Entry(win1)
i3.grid(row=3,column=1,sticky='w',padx='15')
rp=0
win2=w3=e=win3=0
def play():
    global n,g,r,lc,lr,win,regi,root
    root=tk.Toplevel()
    root.title('Tic-Tac-Toe')
    n=g=r=0
    imgf=tk.PhotoImage(file="tb.png")
    tbg=tk.Label(root,image=imgf,bd=-7)
    tbg.image=imgf
    tbg.grid(row=0,column=0,rowspan=6,columnspan=5)
    lc=[['','',''],['','',''],['','','']]
    lr=[[1,2,3],[1,2,3],[1,2,3]]
    win={'x':[0,'X'],'o':[0,'O']}
    def namcha():
        global win,r,g,root,regi
        messagebox.showinfo('Alert','Current game will be lost')
        g-=1
        r=0
        win['x'][1],win['o'][1]='X','O'
        nextgame()
        regi.grid_forget()
        regi=tk.Button(root,text='Register \nNames',command=sta)
        regi.grid(row=2,column=3,columnspan=2)
        regi.config(height=3,width=11)
    def click(r,c):                                                 
        global n,win,lc,lr
        wd=0                                                        
        if lr[r-1][c-1]==c:                                        
            if n%2==0:
               bt=tk.Label(root,text='X',width=4,height=2,font=15)
               bt.grid(row=r-1,column=c-1)
               lc[r-1][c-1]='x'
            elif n%2==1:
               bt=tk.Label(root,text='O',width=4,height=2,font=15)
               bt.grid(row=r-1,column=c-1)
               lc[r-1][c-1]='o'
            n+=1
            lr[r-1][c-1]=None
            
            #checking for win
            if lc[r-1][0]==lc[r-1][1]==lc[r-1][2]!='':
                win[lc[r-1][0]][0]+=1
                messagebox.showinfo('Hurray',(win[lc[r-1][0]][1]+' has won'))
                wd=1
                nextgame()
            elif lc[0][c-1]==lc[1][c-1]==lc[2][c-1]!='':
                messagebox.showinfo('Hurray',(win[lc[0][c-1]][1]+' has won'))
                win[lc[0][c-1]][0]+=1
                wd=1
                nextgame()
            elif lc[0][0]==lc[1][1]==lc[2][2]!='':
                messagebox.showinfo('Hurray',(win[lc[0][0]][1]+' has won'))
                win[lc[0][0]][0]+=1
                nextgame()
            elif lc[0][2]==lc[1][1]==lc[2][0]!='':
                messagebox.showinfo('Hurray',(win[lc[1][1]][1]+' has won'))
                win[lc[1][1]][0]+=1
                nextgame()
            if n==9:
                messagebox.showinfo('Next Time',"It's a draw!")
                nextgame()

    def nextgame():
        global n,win,lc,lr,name1,name2,r,g
        lc=[['','',''],['','',''],['','','']]
        lr=[[1,2,3],[1,2,3],[1,2,3]]
        wd=0 
        g=g+1
        n=0
        label=tk.Label(root,text='Game No.='+str(g)+'\nGames Won:\n'+str(win['x'][1])+':'+str(win['x'][0])+'\n'+str(win['o'][1])+':'+str(win['o'][0]))
        label.grid(row=3,column=0,rowspan=3,columnspan=3)
        bt=tk.Button(root,text=' ',command=lambda:click(1,1),width=7,height=3)
        bt.grid(row=0,column=0,sticky='se')

        bt=tk.Button(root,text=' ',command=lambda:click(1,2),width=7,height=3)
        bt.grid(row=0,column=1,sticky='sew')

        bt=tk.Button(root,text=' ',command=lambda:click(1,3),width=7,height=3)
        bt.grid(row=0,column=2,sticky='sw')

        bt=tk.Button(root,text=' ',command=lambda:click(2,1),width=7,height=3)
        bt.grid(row=1,column=0,sticky='nse')

        bt=tk.Button(root,text=' ',command=lambda:click(2,2),width=7,height=3)
        bt.grid(row=1,column=1,sticky='nsew')

        bt=tk.Button(root,text=' ',command=lambda:click(2,3),width=7,height=3)
        bt.grid(row=1,column=2,sticky='nsw')

        bt=tk.Button(root,text=' ',command=lambda:click(3,1),width=7,height=3)
        bt.grid(row=2,column=0,sticky='ne')

        bt=tk.Button(root,text=' ',command=lambda:click(3,2),width=7,height=3)
        bt.grid(row=2,column=1,sticky='new')

        bt=tk.Button(root,text=' ',command=lambda:click(3,3),width=7,height=3)
        bt.grid(row=2,column=2,sticky='nw')
        if r==0:
            name=tk.Label(root,text='Player \nwith X',width=5)
            name.grid(row=0,column=3)
            name1=tk.Entry(root,width=10)
            name1.grid(row=0,column=4)

            name=tk.Label(root,text='Player \nwith O',width=5)
            name.grid(row=1,column=3)
            name2=tk.Entry(root,width=10)
            name2.grid(row=1,column=4)

        nxtgame=tk.Button(root,text='Next Game\n(Mutual Draw)',width=10,height=2,command=nextgame)
        nxtgame.grid(row=3,column=3,rowspan=2,columnspan=2,sticky='ns')
        nxtgame.config(height=3,width=11)
        sc=tk.Button(root,text='Interchange\nSigns',command=signchange)
        sc.grid(row=5,column=3,rowspan=2,columnspan=2,sticky='n')
        sc.config(height=3,width=11)

    def signchange():
        global g,win
        if win['x'][1]!='X' and win['o'][1]!='O':
            win['x'],win['o']=win['o'],win['x']
            g-=1
            nextgame()
        elif win['x'][1]!='X' and win['o'][1]=='O':
            win['x'],win['o']=win['o'],win['x']
            win['x'][1]='X'
            g-=1
            nextgame()
        elif win['x'][1]=='X' and win['o'][1]!='O':
            win['x'],win['o']=win['o'],win['x']
            win['o'][1]='O'
            g-=1
            nextgame()
        else:
            win['x'],win['o']=win['o'],win['x']
            win['o'][1]='O'
            win['x'][1]='X'
            g-=1
            nextgame()
        name1=tk.Label(root,text=win['x'][1])
        name1.grid(row=0,column=4)
        name2=tk.Label(root,text=win['o'][1])
        name2.grid(row=1,column=4)  

    def sta():
        global win,name1,name2,r,regi
        if r==0:
            name1.grid_forget()
            name2.grid_forget()
            if name1.get()=='' or name2.get()=='':
                if win['x'][1]=='' and win['o'][1]!='':
                    win['o'][1]=name2.get()
                if win['x'][1]!='' and win['o'][1]=='':
                    win['x'][1]=name1.get()
            else:
                win['x'][1]=name1.get()
                win['o'][1]=name2.get()
                
            name1=tk.Label(root,text=win['x'][1])
            name1.grid(row=0,column=4)
            name2=tk.Label(root,text=win['o'][1])
            name2.grid(row=1,column=4)
            label=tk.Label(root,text='Game No.='+str(g)+'\nGames Won:\n'+str(win['x'][1])+':'+str(win['x'][0])+'\n'+str(win['o'][1])+':'+str(win['o'][0]))
            label.grid(row=3,column=0,rowspan=3,columnspan=3)

            regi.grid_forget()
            registered=tk.Button(root,text='Change Names',command=namcha)
            registered.grid(row=2,column=3,columnspan=2)
            r=1
        else:
            name1=tk.Label(root,text=win['x'][1])
            name1.grid(row=0,column=4)
            name2=tk.Label(root,text=win['o'][1])
            name2.grid(row=1,column=4)
            label=tk.Label(root,text='Game No.='+str(g)+'\nGames Won:\n'+str(win['x'][1])+':'+str(win['x'][0])+'\n'+str(win['o'][1])+':'+str(win['o'][0]))
            label.grid(row=3,column=0,rowspan=3,columnspan=3)
    regi=tk.Button(root,text='Register \nNames',command=sta)
    regi.grid(row=2,column=3,columnspan=2,sticky='s')
    regi.config(height=3,width=11)
    nextgame()
    root.mainloop()


u=[]
p=[]
kd=[]
mc.execute('select * from emp_n')
r=mc.fetchall()
for i in r:
    u.append(i[0])
    p.append(i[6])
mc.execute('select empname,empid,emp_n.category,password from emp_n, checks where emp_n.category=checks.category')
k=mc.fetchall()
for j in k:
    kd.append(list(j))

def go_to_admin():
    global win2,fopen,ba1,ba2,ba3,ba4,ba5,ba6,exa,background
    fopen=0
    win2.destroy()
    win2=tk.Toplevel()
    win2.geometry()
    winopen=1
    win2.title('Admin Window')
    img6=tk.PhotoImage(file="ab.png")
    background=tk.Label(win2,image=img6,bd=-7)
    background.image=img6
    background.grid(row=0,column=0,rowspan=2,columnspan=4)
    ba1=tk.Button(win2,text='Search\nRecord',command=s_id)
    ba1.grid(row=0,column=0)
    ba1.config(font=('Kefa',20),height='6',width='25')
    ba2=tk.Button(win2,text='Modify\nRecord',command=mod)
    ba2.grid(row=0,column=1)
    ba2.config(font=('Kefa',20),height='6',width='25')
    ba3=tk.Button(win2,text='Delete\nRecord',command=Del)
    ba3.grid(row=0,column=2)
    ba3.config(font=('Kefa',20),height='6',width='25')
    ba4=tk.Button(win2,text='Add\nRecord',command=Add)
    ba4.grid(row=1,column=0,)
    ba4.config(font=('Kefa',20),height='6',width='25')
    ba5=tk.Button(win2,text='Edit/view\npasskeys',command=Pas)
    ba5.grid(row=1,column=1)
    ba5.config(font=('Kefa',20),height='6',width='25')
    ba6=tk.Button(win2,text='View all\nrecords',command=view)
    ba6.grid(row=1,column=2)
    ba6.config(font=('Kefa',20),height='6',width='25')
    exa=tk.Button(win2, text='Exit', command=excon)
    exa.grid(row=0,column=3,rowspan=2)
    exa.config(font=('Kefa',20),height='7',width='12')
    win2.mainloop()

def excon():
    global winopen,win2,i1,i2,i3,r,u,p
    opi=messagebox.askquestion('Session Termination','Confirm Session Termination')
    if opi=='yes':
        win2.destroy()
        messagebox.showinfo('Session Terminated','You will be redirected to main window')
        winopen=0
        mc.execute('insert into log values(%s,%s,%s)',(eval(i1.get()),'y','Ses_term'))
        db.commit()
        i1.grid_forget()
        i2.grid_forget()
        i3.grid_forget()
        i1=tk.Entry(win1)
        i1.grid(row=1,column=1,sticky='w',padx='15')
        i2=tk.Entry(win1)
        i2.grid(row=2,column=1,sticky='w',padx='15')
        i3=tk.Entry(win1)
        i3.grid(row=3,column=1,sticky='w',padx='15')
        mc.execute('select * from emp_n')
        r=mc.fetchall()
        u=[]
        p=[]
        for i in r:
            u.append(i[0])
            p.append(i[6])
        print(u,p)    
        
    else:
        messagebox.showinfo('Return','You will be redirected to previous session window')

def s_id():
    global win2,r,rp,e,fopen,go_to_admin,background,ba1,ba2,ba3,ba4,ba5,ba6,exa,un
    if fopen==0:
        fopen=1
        ba1.grid_forget()
        ba2.grid_forget()
        ba3.grid_forget()
        ba4.grid_forget()
        ba5.grid_forget()
        ba6.grid_forget()
        exa.grid_forget()
        background.grid_forget()
        img6=tk.PhotoImage(file="abd.png")
        background=tk.Label(win2,image=img6,bd=-7)
        background.image=img6
        background.grid(row=0,column=0,rowspan=10,columnspan=3)
        def Get():
            global rp
            try:
                eid=eval(e.get())
                if u.count(eid)==0:
                    messagebox.showinfo('Error',"Record doesn't exist")
                    mc.execute('insert into log values(%s,%s,%s)',(un,'y','A_search_wr'+str(e.get())))
                    db.commit()
                else:
                    rp=1
                    for j in r:
                        if j[0]==eid:
                            e.grid_forget()
                            mc.execute('insert into log values(%s,%s,%s)',(un,'y','search'+str(e.get())))
                            db.commit()
                            for v in range(9):
                                l=tk.Label(win2,text=j[v])
                                l.grid(row=v+1,column=1)
                                l.config(width='15',font=('Gill Sans',20))
                                bs.grid_forget()
                    l=tk.Button(win2,text='This is the \nrequired record')
                    l.grid(row=3,column=2,rowspan=9,columnspan=2)
                    l.config(font=('Kefa',20))
            except:
                messagebox.showinfo('Error',"Kindly fill empid field correctly")
                mc.execute('insert into log values(%s,%s,%s)',(un,'y','search_error'))
        l=tk.Label(win2,text='Empid')
        l.grid(row=1,column=0)
        l.config(font=('monaco',25),width=15)
        lv=tk.Label(win2,text='Employee  Search')
        lv.grid(row=0,column=0,columnspan=2)
        lv.config(font=('Phosphate',40))
        l=tk.Label(win2,text='Name')
        l.grid(row=2,column=0)
        l.config(font=('monaco',25),width=15)
        l=tk.Label(win2,text='Designation')
        l.grid(row=3,column=0)
        l.config(font=('monaco',25),width=15)
        l=tk.Label(win2,text='Department')
        l.grid(row=4,column=0)
        l.config(font=('monaco',25),width=15)
        l=tk.Label(win2,text='Salary')
        l.grid(row=5,column=0)
        l.config(font=('monaco',25),width=15)
        l=tk.Label(win2,text='Category')
        l.grid(row=6,column=0)
        l.config(font=('monaco',25),width=15)
        l=tk.Label(win2,text='Pass')
        l.grid(row=7,column=0)
        l.config(font=('monaco',25),width=15)
        l=tk.Label(win2,text='Address')
        l.grid(row=8,column=0)
        l.config(font=('monaco',25),width=15)
        l=tk.Label(win2,text='Phone')
        l.grid(row=9,column=0)
        l.config(font=('monaco',25),width=15)
        e=tk.Entry(win2)
        e.grid(row=1,column=1)
        bs=tk.Button(win2,text='Go',command=Get)
        bs.grid(row=1,column=2)
        bs.config(font=('kefa',20),width='10')

        b=tk.Button(win2,text='Return To\nAdmin Window',command=go_to_admin)
        b.grid(row=0,column=2)
        b.config(font=('kefa',20))
    else:
        messagebox.showinfo('Error','Another task is going on\nFinish it first')   
def mod():
    global win2,r,rp,e,fopen,go_to_admin,background,ba1,ba2,ba3,ba4,ba5,ba6,exa,un,u,p
    if fopen==0:
            fopen=1
            ba1.grid_forget()
            ba2.grid_forget()
            ba3.grid_forget()
            ba4.grid_forget()
            ba5.grid_forget()
            ba6.grid_forget()
            exa.grid_forget()
            background.grid_forget()
            img6=tk.PhotoImage(file="abm.png")
            background=tk.Label(win2,image=img6,bd=-7)
            background.image=img6
            background.grid(row=0,column=0,rowspan=10,columnspan=4)
            l=tk.Label(win2,text='Empid')
            l.grid(row=1,column=0)
            l.config(font=('monaco',25),width=15)
            lv=tk.Label(win2,text='Employee  Detail  Modification')
            lv.grid(row=0,column=0,columnspan=2)
            lv.config(font=('Phosphate',40))
            l=tk.Label(win2,text='Name')
            l.grid(row=2,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Designation')
            l.grid(row=3,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Department')
            l.grid(row=4,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Salary')
            l.grid(row=5,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Category')
            l.grid(row=6,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Pass')
            l.grid(row=7,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Address')
            l.grid(row=8,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Phone')
            l.grid(row=9,column=0)
            l.config(font=('monaco',25),width=15)
            e=tk.Entry(win2)
            e.grid(row=1,column=1)
            def Get():
                try:
                    eid=eval(e.get())
                    if u.count(eid)==0:
                        messagebox.showinfo('Error',"Record doesn't exist")
                        mc.execute('insert into log values(%s,%s,%s)',(un,'y','A_m_wr'+str(e.get())))
                        db.commit()
                    else:
                        bs.grid_forget()
                        for j in r:
                            if j[0]==eid:
                                e.grid_forget()
                                req_dat=list(j)
                                print(req_dat)
                                for v in range(9):
                                    l=tk.Label(win2,text=j[v])
                                    l.grid(row=v+1,column=1)
                                    l.config(width='15',font=('Gill Sans',20))
                                mc.execute('insert into log values(%s,%s,%s)',(un,'y','A_d_get'))
                                db.commit()
                                   
                                def copy(x):
                                    if x==1:
                                        l1.insert(0,req_dat[1])
                                    elif x==2:    
                                        l2.insert(0,req_dat[2])
                                    elif x==3:    
                                        l3.insert(0,req_dat[3])
                                    elif x==4:
                                        l4.insert(0,req_dat[4])
                                    elif x==5:    
                                        l5.insert(0,req_dat[5])
                                    elif x==6:    
                                        l6.insert(0,req_dat[6])
                                    elif x==7:    
                                        l7.insert(0,req_dat[7])
                                    elif x==8:
                                        l8.insert(0,req_dat[8])
                                bs.grid_forget()
                                l1=tk.Entry(win2)
                                l1.grid(row=2,column=2)
                                l2=tk.Entry(win2)
                                l2.grid(row=3,column=2)
                                l3=tk.Entry(win2)
                                l3.grid(row=4,column=2)
                                l4=tk.Entry(win2)
                                l4.grid(row=5,column=2)
                                l5=tk.Entry(win2)
                                l5.grid(row=6,column=2)
                                l6=tk.Entry(win2)
                                l6.grid(row=7,column=2)
                                l7=tk.Entry(win2)
                                l7.grid(row=8,column=2)
                                l8=tk.Entry(win2)
                                l8.grid(row=9,column=2)
                                b1=tk.Button(win2,text='Copy',command=lambda:copy(1))
                                b1.grid(row=2,column=3)
                                b2=tk.Button(win2,text='Copy',command=lambda:copy(2))
                                b2.grid(row=3,column=3)
                                b3=tk.Button(win2,text='Copy',command=lambda:copy(3))
                                b3.grid(row=4,column=3)
                                b4=tk.Button(win2,text='Copy',command=lambda:copy(4))
                                b4.grid(row=5,column=3)
                                b5=tk.Button(win2,text='Copy',command=lambda:copy(5))
                                b5.grid(row=6,column=3)
                                b6=tk.Button(win2,text='Copy',command=lambda:copy(6))
                                b6.grid(row=7,column=3)
                                b7=tk.Button(win2,text='Copy',command=lambda:copy(7))
                                b7.grid(row=8,column=3)
                                b8=tk.Button(win2,text='Copy',command=lambda:copy(8))
                                b8.grid(row=9,column=3)
                                b1.config(font=('Kefa',20))
                                b2.config(font=('Kefa',20))
                                b3.config(font=('Kefa',20))
                                b4.config(font=('Kefa',20))
                                b5.config(font=('Kefa',20))
                                b6.config(font=('Kefa',20))
                                b7.config(font=('Kefa',20))
                                b8.config(font=('Kefa',20))
                        def con():
                            query="update emp_n set empname=%s,designation=%s,department=%s,salary=%s, category=%s,pass=%s,address=%s,phone=%s where empid=%s"
                            try:
                                mc.execute(query,(l1.get(),l2.get(),l3.get(),eval(l4.get()),l5.get(),l6.get(),l7.get(),eval(l8.get()),eid))
                                db.commit()
                                messagebox.showinfo('Info','Emp data modified successfully')
                                mc.execute('insert into log values(%s,%s,%s)',(un,'y','E_d_ch'))
                                db.commit()
                                mc.execute('select * from emp_n')
                                r=mc.fetchall()
                                u=[]
                                p=[]
                                for i in r:
                                    u.append(i[0])
                                    p.append(i[6])
                                l=tk.Label(win2,text=l1.get())
                                l.grid(row=2,column=2)
                                l.config(width='15',font=('Gill Sans',20))
                                l=tk.Label(win2,text=l2.get())
                                l.grid(row=3,column=2)
                                l.config(width='15',font=('Gill Sans',20))
                                l=tk.Label(win2,text=l3.get())
                                l.grid(row=4,column=2)
                                l.config(width='15',font=('Gill Sans',20))
                                l=tk.Label(win2,text=l4.get())
                                l.grid(row=5,column=2)
                                l.config(width='15',font=('Gill Sans',20))
                                l=tk.Label(win2,text=l5.get())
                                l.grid(row=6,column=2)
                                l.config(width='15',font=('Gill Sans',20))
                                l=tk.Label(win2,text=l6.get())
                                l.grid(row=7,column=2)
                                l.config(width='15',font=('Gill Sans',20))
                                l=tk.Label(win2,text=l7.get())
                                l.grid(row=8,column=2)
                                l.config(width='15',font=('Gill Sans',20))
                                l=tk.Label(win2,text=l8.get())
                                l.grid(row=9,column=2)
                                l.config(width='15',font=('Gill Sans',20))
                                l=tk.Button(win2,text='Column 2-\nOriginal Data\n\nColumn3-\nModified Data')
                                l.grid(row=3,column=3,rowspan=9)
                                l.config(font=('Kefa',20))
                                l1.grid_forget()
                                l2.grid_forget()
                                l3.grid_forget()
                                l4.grid_forget()
                                l5.grid_forget()
                                l6.grid_forget()
                                l7.grid_forget()
                                l8.grid_forget()
                                b1.grid_forget()
                                b2.grid_forget()
                                b3.grid_forget()
                                b4.grid_forget()
                                b5.grid_forget()
                                b6.grid_forget()
                                b7.grid_forget()
                                b8.grid_forget()
                                bt.grid_forget()
                                
                            except:
                                messagebox.showinfo('Error',"Kindly recheck entries\nThere is error\nThese values can't be inserted")
                                mc.execute('insert into log values(%s,%s,%s)',(un,'y','Mod_Data_er'))
                                db.commit()
                        bt=tk.Button(win2,text='Confirm Changes',command=con)
                        bt.grid(row=0,column=2)
                        bt.config(font=('kefa',20))
                except:
                    messagebox.showinfo('Error','Kindly Enter Empid')
                    
                    
            bs=tk.Button(win2,text='Go',command=Get)
            bs.grid(row=1,column=3)
            bs.config(font=('kefa',20),width=10)

            b=tk.Button(win2,text='Return To\nAdmin Window',command=go_to_admin)
            b.grid(row=0,column=3)
            b.config(font=('kefa',20))
    else:
        messagebox.showinfo('Error','Another task is going on\nFinish it first')
        
def Add():
    global rp,fopen,go_to_admin,background,ba1,ba2,ba3,ba4,ba5,ba6,exa,un,u,p
    if fopen==0:
            fopen=1
            ba1.grid_forget()
            ba2.grid_forget()
            ba3.grid_forget()
            ba4.grid_forget()
            ba5.grid_forget()
            ba6.grid_forget()
            exa.grid_forget()
            background.grid_forget()
            img6=tk.PhotoImage(file="abd.png")
            background=tk.Label(win2,image=img6,bd=-7)
            background.image=img6
            background.grid(row=0,column=0,rowspan=11,columnspan=3)
            lv=tk.Label(win2,text='Employee  Addition')
            lv.grid(row=0,column=0,columnspan=2)
            lv.config(font=('Phosphate',40))
            l=tk.Label(win2,text='Empid')
            l.grid(row=1,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Empname')
            l.grid(row=2,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Designation')
            l.grid(row=3,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Department')
            l.grid(row=4,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Salary')
            l.grid(row=5,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Category')
            l.grid(row=6,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Pass')
            l.grid(row=7,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Address')
            l.grid(row=8,column=0)
            l.config(font=('monaco',25),width=15)
            l=tk.Label(win2,text='Phone')
            l.grid(row=9,column=0)
            l.config(font=('monaco',25),width=15)
            l1=tk.Entry(win2)
            l1.grid(row=1,column=1)
            l2=tk.Entry(win2)
            l2.grid(row=2,column=1)
            l3=tk.Entry(win2)
            l3.grid(row=3,column=1)
            l4=tk.Entry(win2)
            l4.grid(row=4,column=1)
            l5=tk.Entry(win2)
            l5.grid(row=5,column=1)
            l6=tk.Entry(win2)
            l6.grid(row=6,column=1)
            l7=tk.Entry(win2)
            l7.grid(row=7,column=1)
            l8=tk.Entry(win2)
            l8.grid(row=8,column=1)
            l9=tk.Entry(win2)
            l9.grid(row=9,column=1)
            def adgo():
                try:
                    dat=tuple([eval(l1.get()),l2.get(),l3.get(),l4.get(),eval(l5.get()),l6.get(),l7.get(),l8.get(),eval(l9.get())])
                    mc.execute('insert into emp_n values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',dat)
                    db.commit()
                    mc.execute('insert into log values(%s,%s,%s)',(un,'y','Add_rec'))
                    db.commit()
                    lt=tk.Button(win2,text='This record \nhas been added')
                    lt.grid(row=3,column=2,rowspan=2,columnspan=2)
                    lt.config(font=('Kefa',20))
                    mc.execute('select * from emp_n')
                    r=mc.fetchall()
                    u=[]
                    p=[]
                    for i in r:
                        u.append(i[0])
                        p.append(i[6])
                    for j in r:
                        if j[0]==eval(l1.get()):
                            l1.grid_forget()
                            l2.grid_forget()
                            l3.grid_forget()
                            l4.grid_forget()
                            l5.grid_forget()
                            l6.grid_forget()
                            l7.grid_forget()
                            l8.grid_forget()
                            l9.grid_forget()
                            for v in range(9):
                                l=tk.Label(win2,text=j[v])
                                l.grid(row=v+1,column=1)
                                l.config(width='15',font=('Gill Sans',20))
                                bt.grid_forget()
                except:
                    messagebox.showinfo('Error',"Kindly recheck entries\nThere is error\nThese values can't be inserted")
                    mc.execute('insert into log values(%s,%s,%s)',(un,'y','Add_Data_er'))
                    db.commit()
            bt=tk.Button(win2,text='Confirm Addn',command=adgo)
            bt.grid(row=0,column=2)
            bt.config(font=('Kefa',20))

            b=tk.Button(win2,text='Return To\nAdmin Window',command=go_to_admin)
            b.grid(row=2,column=2,rowspan=2)
            b.config(font=('Kefa',20))
    else:
        messagebox.showinfo('Error','Another task is going on\nFinish it first')
def Pas():
    global w3,winopen,win3,un
    try:
        win3.destroy()
        win3=tk.Toplevel()
        win3.geometry()
        mc.execute('insert into log values(%s,%s,%s)',(un,'y','View_passkey'))
        db.commit()
        win3.title('Passkeys')
        img5=tk.PhotoImage(file="k2.png")
        background=tk.Label(win3,image=img5,bd=-2)
        background.grid(row=0,column=0,rowspan=4,columnspan=3)
        w3=1
        l1=tk.Label(win3,text='Category')
        l1.grid(row=0,column=0)
        l2=tk.Label(win3,text='Passkey')
        l2.grid(row=0,column=1)
        l1.config(font=('Gill Sans',21),bg='black',fg='white')
        l2.config(font=('Gill Sans',21),bg='black',fg='white')
        def p_e():
            e1=tk.Entry(win3)
            e1.grid(row=1,column=2)
            e2=tk.Entry(win3)
            e2.grid(row=2,column=2)
            def p_c():
                try:
                    if len(str(e1.get().replace(' ','')))!=0 and len(str(e2.get().replace(' ','')))!=0:
                        mc.execute("update checks set password=%s where category='A'",tuple([e1.get()]))
                        db.commit()
                        mc.execute("update checks set password=%s where category='E'",tuple([e2.get()]))
                        db.commit()
                        messagebox.showinfo('Info',"Keys updated successfully")
                        mc.execute('insert into log values(%s,%s,%s)',(un,'y','Mod_passkey'))
                        db.commit()
                    else:
                        messagebox.showinfo('Error',"Keys can't be empty")
                except:
                    messagebox.showinfo('Error',"Kindly recheck entries\nThere is error\nThese values can't be inserted")
                    mc.execute('insert into log values(%s,%s,%s)',(un,'y','Passkey_ch_error'))
                    db.commit()
            bt=tk.Button(win3,text='Confirm',command=p_c)
            bt.grid(row=3,column=2)
            bt.config(width='10',font=('Kefa',18))
        mc.execute('select * from checks')
        pkg=mc.fetchall()
        for j in range(2):
            for v in range(2):
                l=tk.Label(win3,text=pkg[j][v])
                l.grid(row=j+1,column=v)
                l.config(font=('monaco',17),bg='indian red',fg='white')
        b=tk.Button(win3,text='Edit',command=p_e)
        b.grid(row=3,column=0)
        b.config(width='10',font=('Kefa',18))
        win3.mainloop()
    except:
        win3=tk.Toplevel()
        win3.geometry()
        win3.title('Passkeys')
        img=tk.PhotoImage(file="k2.png")
        background=tk.Label(win3,image=img,bd=-7)
        background.grid(row=0,column=0,rowspan=4,columnspan=3)
        w3=1
        l1=tk.Label(win3,text='Category')
        l1.grid(row=0,column=0)
        l1.config(font=('Gill Sans',21),bg='black',fg='white')
        l2=tk.Label(win3,text='Passkey')
        l2.grid(row=0,column=1)
        l2.config(font=('Gill Sans',21),bg='black',fg='white')
        def p_e():
            e1=tk.Entry(win3)
            e1.grid(row=1,column=2)
            e2=tk.Entry(win3)
            e2.grid(row=2,column=2)
            def p_c():
                try:
                    if len(str(e1.get().replace(' ','')))!=0 and len(str(e2.get().replace(' ','')))!=0:
                        mc.execute("update checks set password=%s where category='A'",tuple([e1.get()]))
                        db.commit()
                        mc.execute("update checks set password=%s where category='E'",tuple([e2.get()]))
                        db.commit()
                        messagebox.showinfo('Info',"Keys updated successfully")
                        mc.execute('insert into log values(%s,%s,%s)',(un,'y','Mod_passkey'))
                        db.commit()    
                    else:
                        messagebox.showinfo('Error',"Keys can't be empty")
                except:
                    messagebox.showinfo('Error',"Kindly recheck entries\nThere is error\nThese values can't be inserted")
                    mc.execute('insert into log values(%s,%s,%s)',(un,'y','Passkey_ch_error'))
                    db.commit()
            bt=tk.Button(win3,text='Confirm',command=p_c)
            bt.grid(row=3,column=2)
            bt.config(width='10',font=('Kefa',18))
        mc.execute('select * from checks')
        pkg=mc.fetchall()
        for j in range(2):
            for v in range(2):
                l=tk.Label(win3,text=pkg[j][v])
                l.grid(row=j+1,column=v)
                l.config(font=('monaco',17),bg='indian red',fg='white')
        b=tk.Button(win3,text='Edit',command=p_e)
        b.grid(row=3,column=0)
        b.config(width='10',font=('Kefa',18))
        win3.mainloop()
        
def Del():
    global win2,r,rp,fopen,go_to_admin,background,ba1,ba2,ba3,ba4,ba5,ba6,exa,un,u,p
    if fopen==0:
            fopen=1
            ba1.grid_forget()
            ba2.grid_forget()
            ba3.grid_forget()
            ba4.grid_forget()
            ba5.grid_forget()
            ba6.grid_forget()
            exa.grid_forget()
            background.grid_forget()
            img6=tk.PhotoImage(file="abd.png")
            background=tk.Label(win2,image=img6,bd=-7)
            background.image=img6
            background.grid(row=0,column=0,rowspan=11,columnspan=3)
            e=tk.Entry(win2)
            e.grid(row=1,column=1)
            def Get():
                global u,p,r
                try:
                    eid=eval(e.get())
                    if u.count(eid)==0:
                         messagebox.showinfo('Error',"Record doesn't exist")
                         mc.execute('insert into log values(%s,%s,%s)',(un,'y','A_m_wr'))
                         db.commit()
                    else:
                        bs.grid_forget()
                        for j in r:
                            if j[0]==eid:
                                e.grid_forget()
                                for v in range(9):
                                    l=tk.Label(win2,text=j[v])
                                    l.grid(row=v+1,column=1)
                                    l.config(width='15',height='1',font=('Gill Sans',20))
                                    rp=1
                                
                                mc.execute("delete from emp_n where empid=%s",tuple([eid]))
                                db.commit()
                                mc.execute('insert into log values(%s,%s,%s)',(un,'y','Del_rec'+str(e.get())))
                                db.commit()
                                l=tk.Button(win2,text='This record\nhas been deleted')
                                l.grid(row=4,column=2,rowspan=2)
                                l.config(font=('Kefa',20))
                                bs.grid_forget()
                                break
                        mc.execute('select * from emp_n')
                        r=mc.fetchall()
                        u=[]
                        p=[]
                        for i in r:
                            u.append(i[0])
                            p.append(i[6])    
                except:
                    messagebox.showinfo('Error','Kindly Enter Empid')
            b=tk.Button(win2,text='Return To\nAdmin Window',command=go_to_admin)
            b.grid(row=2,column=2,rowspan=2)
            b.config(font=('Kefa',20))
            lv=tk.Label(win2,text='Employee  Deletion')
            lv.grid(row=0,column=0,columnspan=2)
            lv.config(font=('Phosphate',40))    
            l=tk.Label(win2,text='Empid')
            l.grid(row=1,column=0)
            l.config(font=('monaco',25),width=10)
            l=tk.Label(win2,text='Name')
            l.grid(row=2,column=0)
            l.config(font=('monaco',25),width=10)
            l=tk.Label(win2,text='Designation')
            l.grid(row=3,column=0)
            l.config(font=('monaco',25),width=10)
            l=tk.Label(win2,text='Department')
            l.grid(row=4,column=0)
            l.config(font=('monaco',25),width=10)
            l=tk.Label(win2,text='Salary')
            l.grid(row=5,column=0)
            l.config(font=('monaco',25),width=10)
            l=tk.Label(win2,text='Category')
            l.grid(row=6,column=0)
            l.config(font=('monaco',25),width=10)
            l=tk.Label(win2,text='Pass')
            l.grid(row=7,column=0)
            l.config(font=('monaco',25),width=10)
            l=tk.Label(win2,text='Address')
            l.grid(row=8,column=0)
            l.config(font=('monaco',25),width=10)
            l=tk.Label(win2,text='Phone')
            l.grid(row=9,column=0)
            l.config(font=('monaco',25),width=10)
            bs=tk.Button(win2,text='Delete',command=Get)
            bs.grid(row=4,column=2)
            bs.config(font=('Kefa',20),height='2',width='10')

    else:
        messagebox.showinfo('Error','Another task is going on\nFinish it first')
def view():
    global go_to_admin,fopen,background,ba1,ba2,ba3,ba4,ba5,ba6,exa,un
    if fopen==0:
        ba1.grid_forget()
        ba2.grid_forget()
        ba3.grid_forget()
        ba4.grid_forget()
        ba5.grid_forget()
        ba6.grid_forget()
        exa.grid_forget()
        fopen=1
        mc.execute('select * from emp_n')
        r=mc.fetchall()
        mc.execute('insert into log values(%s,%s,%s)',(un,'y','view_rec'))
        db.commit()
        background.grid_forget()
        img6=tk.PhotoImage(file="abf.png")
        background=tk.Label(win2,image=img6,bd=-7)
        background.image=img6
        background.grid(row=0,column=0,rowspan=12,columnspan=len(r)*2+1)
        lv=tk.Label(win2,text='Details of All Current Employees')
        lv.grid(row=0,column=0,columnspan=len(r)*2+1)
        lv.config(font=('Phosphate',40),height=1)
        l=tk.Label(win2,text='EMPID')
        l.grid(row=1,column=0)
        l.config(font=('monaco',25),width=10)
        l=tk.Label(win2,text='NAME')
        l.grid(row=2,column=0)
        l.config(font=('monaco',25),width=10)
        l=tk.Label(win2,text='DESIGNATION')
        l.grid(row=3,column=0)
        l.config(font=('monaco',25),width=10)
        l=tk.Label(win2,text='DEPARTMENT')
        l.grid(row=4,column=0)
        l.config(font=('monaco',25),width=10)
        l=tk.Label(win2,text='SALARY')
        l.grid(row=5,column=0)
        l.config(font=('monaco',25),width=10)
        l=tk.Label(win2,text='CATEGORY')
        l.grid(row=6,column=0)
        l.config(font=('monaco',25),width=10)
        l=tk.Label(win2,text='PASS')
        l.grid(row=7,column=0)
        l.config(font=('monaco',25),width=10)
        l=tk.Label(win2,text='ADDRESS')
        l.grid(row=8,column=0)
        l.config(font=('monaco',25),width=10)
        l=tk.Label(win2,text='PHONE')
        l.grid(row=9,column=0)
        l.config(font=('monaco',25),width=10)
        row=0
        
        img7=tk.PhotoImage(file="bov.png")
        for j in r:
            for v in range(9):
                l=tk.Label(win2,text=j[v])
                l.grid(row=v+1,column=2*row+2)
                l.config(width='15',height='1',font=('Gill Sans',20))
                bor=tk.Label(win2,image=img7,bd=-7)
                bor.image=img7
                bor.grid(row=1,column=2*row+1,rowspan=10)
                bor.config(height='1000')
            row+=1
        b=tk.Button(win2,text='Return To Admin Window',command=go_to_admin)
        b.grid(row=11,column=(row+1)//2,columnspan=4)
        b.config(font=('kefa',22))
    else:
        messagebox.showinfo('Error','Another task is going on\nFinish it first')            
            
def mainprg():
    global i1,i2,i3,u,p,r,winopen,kd,win2,background,ba1,ba2,ba3,ba4,ba5,ba6,exa,un
    try:
        un=eval(i1.get())
        pw=i2.get()
        pk=i3.get()
        mc=db.cursor()
        if u.count(un)==0:
            messagebox.showinfo('Error',"User doesn't exist")
            mc.execute('insert into log values(%s,%s,%s)',(None,'c','w_user '+str(un)))
            db.commit()
        else:
            if winopen==0:
                i=u.index(un)
                if p[i]==pw:
                    winopen=1
                    if pk=='':
                       messagebox.showinfo('Session info','Welcome to Reception Session')
                       mc.execute('insert into log values(%s,%s,%s)',(un,'y','R_win'))
                       db.commit()
                       win2=tk.Toplevel()
                       win2.geometry('1280x720')
                       img4=tk.PhotoImage(file="bo.png")
                       bor=tk.Label(win2,image=img4,bd=-7)
                       bor.image=img4
                       img3=tk.PhotoImage(file="rw1.png")
                       background=tk.Label(win2,image=img3,bd=-7)
                       background.image=img3
                       background.grid(row=0,column=0,rowspan=(len(r)*2+3),columnspan=4)
                       win2.title('Reception Window')
                       lv=tk.Label(win2,text='Details of All Current Employees')
                       lv.grid(row=0,column=0,columnspan=4)
                       lv.config(font=('Phosphate',40),height=1)
                       l=tk.Label(win2,text='Name')
                       l.grid(row=1,column=0)
                       l.config(font=('Gill Sans',25),width=20)
                       l=tk.Label(win2,text='Designation')
                       l.grid(row=1,column=1)
                       l.config(font=('Gill Sans',25),width=20)
                       l=tk.Label(win2,text='Department')
                       l.grid(row=1,column=2)
                       l.config(font=('Gill Sans',25),width=20)
                       l=tk.Label(win2,text='Phone')
                       l.grid(row=1,column=3)
                       l.config(font=('Gill Sans',25),width=20)
                       mc.execute('select empname, designation, department,phone from emp_n')
                       data=mc.fetchall()
                       row=len(data)
                       for j in range(len(data)):
                           for v in range(4):
                               l=tk.Label(win2, text=data[j][v])
                               l.grid(row=(j+1)*2+1,column=v)
                               l.config(font=('Monaco',18),height='1',pady=0,bg='indian red',fg='white',width=20)
                               bor=tk.Label(win2,image=img4,bd=-2)
                               bor.image=img4
                               bor.grid(row=(j+1)*2,column=0,columnspan=4)
                               bor.config(width=1280,bd=-2)
                       ex=tk.Button(win2, text='Exit', command=excon)
                       ex.grid(row=2*len(r)+2,column=1,columnspan=2)
                       ex.config(font=('Kefa',22),width=20)
                    else:
                        kf=0
                        for j in kd:
                            if j[3]==pk and j[1]==un:
                                kf=1
                                if j[2]=='E':
                                    mc.execute('select * from emp_n')
                                    r=mc.fetchall()
                                    messagebox.showinfo('Session info','Welcome to Employee Session')
                                    mc.execute('insert into log values(%s,%s,%s)',tuple([un,'y','E_win']))
                                    db.commit()
                                    win2=tk.Toplevel()
                                    win2.geometry()
                                    img2=tk.PhotoImage(file="slide-image-2.png")
                                    background=tk.Label(win2,image=img2,bd=-7)
                                    background.grid(row=0,column=0,rowspan=11,columnspan=4)
                                    win2.title('Employee Window')
                                    lv=tk.Label(win2,text='Your Details')
                                    lv.grid(row=0,column=0,columnspan=4)
                                    lv.config(font=('Phosphate',30))
                                    l=tk.Label(win2,text='Empid')
                                    l.grid(row=1,column=0,sticky='e')
                                    l.config(bg='gray34',font=('Gill Sans',21))
                                    l=tk.Label(win2,text='Name')
                                    l.grid(row=2,column=0,sticky='e')
                                    l.config(bg='gray34',font=('Gill Sans',21))
                                    l=tk.Label(win2,text='Designation')
                                    l.grid(row=3,column=0,sticky='e')
                                    l.config(bg='gray34',font=('Gill Sans',21))
                                    l=tk.Label(win2,text='Department')
                                    l.grid(row=4,column=0,sticky='e')
                                    l.config(bg='gray34',font=('Gill Sans',21))
                                    l=tk.Label(win2,text='Salary')
                                    l.grid(row=5,column=0,sticky='e')
                                    l.config(bg='gray34',font=('Gill Sans',21))
                                    l=tk.Label(win2,text='Category')
                                    l.grid(row=6,column=0,sticky='e')
                                    l.config(bg='gray34',font=('Gill Sans',21))
                                    l=tk.Label(win2,text='Pass')
                                    l.grid(row=7,column=0,sticky='e')
                                    l.config(bg='gray34',font=('Gill Sans',21))
                                    l=tk.Label(win2,text='Address')
                                    l.grid(row=8,column=0,sticky='e')
                                    l.config(bg='gray34',font=('Gill Sans',21))
                                    l=tk.Label(win2,text='Phone')
                                    l.grid(row=9,column=0,sticky='e')
                                    l.config(bg='gray34',font=('Gill Sans',21))
                                    for j in r:
                                        if j[0]==un:
                                            req_dat=list(j)
                                            for v in range(9):
                                                l=tk.Label(win2,text=j[v])
                                                l.grid(row=v+1,column=1,sticky='w',padx=6)
                                                l.config(width='10',font=('monaco',17))
                                            break
                                
                                    
                                    def E_edit():
                
                                        e_n=tk.Entry(win2)
                                        e_n.grid(row=2,column=2)
                                        e_n.config(width='20')
                                        p=tk.Entry(win2)
                                        p.grid(row=7,column=2)
                                        p.config(width='20')
                                        a=tk.Entry(win2)
                                        a.grid(row=8,column=2)
                                        a.config(width='20')
                                        ph=tk.Entry(win2)
                                        ph.grid(row=9,column=2)
                                        ph.config(width='20')
                                        def copy(x):
                                            if x==1:
                                                e_n.insert(0,req_dat[1])
                                            elif x==6:
                                                p.insert(0,req_dat[6])
                                            elif x==7:
                                                a.insert(0,req_dat[7])
                                            elif x==8:
                                                ph.insert(0,req_dat[8])
                                                
                                        b1=tk.Button(win2,text='Copy',command=lambda:copy(1))
                                        b1.grid(row=2,column=3)
                                        b2=tk.Button(win2,text='Copy',command=lambda:copy(6))
                                        b2.grid(row=7,column=3)
                                        b3=tk.Button(win2,text='Copy',command=lambda:copy(7))
                                        b3.grid(row=8,column=3)
                                        b4=tk.Button(win2,text='Copy',command=lambda:copy(8))
                                        b4.grid(row=9,column=3)
                                        b1.config(font=('kefa',19))
                                        b2.config(font=('kefa',19))
                                        b3.config(font=('kefa',19))
                                        b4.config(font=('kefa',19))
                                        
                                        def e_update():
                                            query="update emp_n set empname=%s, pass=%s,address=%s,phone=%s where empid=%s"
                                            try:
                                                mc.execute(query,(e_n.get(),p.get(),a.get(),eval(ph.get()),un))
                                                db.commit()
                                                messagebox.showinfo('Info','Emp data modified successfully\nYou are now viewing new Data')
                                                mc.execute('insert into log values(%s,%s,%s)',(un,'y','E_d_ch'))
                                                db.commit()
                                                l1=tk.Label(win2,text=e_n.get())
                                                l1.grid(row=2,column=1,sticky='w',padx=6)
                                                l1.config(width='10',font=('monaco',17))
                                                l2=tk.Label(win2,text=p.get())
                                                l2.grid(row=7,column=1,sticky='w',padx=6)
                                                l2.config(width='10',font=('monaco',17))
                                                l3=tk.Label(win2,text=a.get())
                                                l3.grid(row=8,column=1,sticky='w',padx=6)
                                                l3.config(width='10',font=('monaco',17))
                                                l4=tk.Label(win2,text=ph.get())
                                                l4.grid(row=9,column=1,sticky='w',padx=6)
                                                l4.config(width='10',font=('monaco',17))
                                                b1.grid_forget()
                                                b2.grid_forget()
                                                b3.grid_forget()
                                                b4.grid_forget()
                                                bs.grid_forget()
                                                e_n.grid_forget()
                                                p.grid_forget()
                                                a.grid_forget()
                                                ph.grid_forget()
                                                
                                            
                                            except:
                                                messagebox.showinfo('Error',"Kindly recheck entries\nThere is error\nThese values can't be inserted")
                                                mc.execute('insert into log values(%s,%s,%s)',(un,'y','Dat_er'))
                                                db.commit()
                
                                        bs=tk.Button(win2,text='Update',command=e_update)
                                        bs.grid(row=10,column=3)
                                        bs.config(font=('kefa',19))
                                    
                                    b=tk.Button(win2,text='Edit Profile',command=E_edit)
                                    b.grid(row=10,column=0)
                                    b.config(font=('kefa',19))
                                    ex=tk.Button(win2, text='Exit from here only', command=excon)
                                    ex.grid(row=10,column=1,columnspan=2)
                                    ex.config(font=('Kefa',19))
                                    win2.mainloop()        
       
                                elif j[2]=='A':
                                    messagebox.showinfo('Session info','Welcome to Admin Session')
                                    mc.execute('insert into log values(%s,%s,%s)',(un,'y','A_win'))
                                    db.commit()
                                    win2=tk.Toplevel()
                                    win2.geometry()
                                    winopen=1
                                    win2.title('Admin Window')
                                    img6=tk.PhotoImage(file="ab.png")
                                    background=tk.Label(win2,image=img6,bd=-7)
                                    background.image=img6
                                    background.grid(row=0,column=0,rowspan=2,columnspan=4)
                                    ba1=tk.Button(win2,text='Search\nRecord',command=s_id)
                                    ba1.grid(row=0,column=0)
                                    ba1.config(font=('Kefa',20),height='6',width='25')
                                    ba2=tk.Button(win2,text='Modify\nRecord',command=mod)
                                    ba2.grid(row=0,column=1)
                                    ba2.config(font=('Kefa',20),height='6',width='25')
                                    ba3=tk.Button(win2,text='Delete\nRecord',command=Del)
                                    ba3.grid(row=0,column=2)
                                    ba3.config(font=('Kefa',20),height='6',width='25')
                                    ba4=tk.Button(win2,text='Add\nRecord',command=Add)
                                    ba4.grid(row=1,column=0,)
                                    ba4.config(font=('Kefa',20),height='6',width='25')
                                    ba5=tk.Button(win2,text='Edit/view\npasskeys',command=Pas)
                                    ba5.grid(row=1,column=1)
                                    ba5.config(font=('Kefa',20),height='6',width='25')
                                    ba6=tk.Button(win2,text='View all\nrecords',command=view)
                                    ba6.grid(row=1,column=2)
                                    ba6.config(font=('Kefa',20),height='6',width='25')
                                    exa=tk.Button(win2, text='Exit', command=excon)
                                    exa.grid(row=0,column=3,rowspan=2)
                                    exa.config(font=('Kefa',20),height='6',width='12')
                                    win2.mainloop()

                        if kf==0:
                            winopen=0
                            messagebox.showinfo('Error',"Wrong passkey")
                            mc.execute('insert into log values(%s,%s,%s)',(un,'y','wrong_k'))
                            db.commit()
                       
                else:
                    messagebox.showinfo('Error',"Wrong username/passwd")
                    mc.execute('insert into log values(%s,%s,%s)',(un,'n','Blocked'))
                    db.commit()
            elif winopen==1:
                messagebox.showinfo('Oops','Another session is already open\nEnd it to start another')
                mc.execute('insert into log values(%s,%s,%s)',(un,'c','n_ses'))
                db.commit()
    except:
        messagebox.showinfo('Error','Kindly Fill Empid and Password field')
b2=tk.Button(win1,text='Break Time, Play Time',command=play)
b2.grid(row=5,column=0,columnspan=2)
b2.config(font=('Kefa',20))
b1=tk.Button(win1,text='Enter',command=mainprg)
b1.grid(row=4,column=0,columnspan=2)
b1.config(font=('Kefa',20))
win1.mainloop()


