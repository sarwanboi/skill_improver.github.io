__author__ = "Sarwan Yadav"
__name__ = "Skill Improver"
__version__ = "1.2"
###########################################
    # IMPORTING IMPORTANT LIBRARIES
import random
import time
import threading
import webbrowser
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Progressbar

    # IMPORTING IMPORTANT REQUIRMENTS
###########################################




# -->> IN WORDS HAVING A WORDS DICTIONARY ABOUT 400 WORDS

words = ['ability','artist','able','about','above','accept','according','account','across','act','action','activity','actually','add','address','administration','admit','adult','affect','after','again','against',
         'age','agency','agent','ago','agree','agreement','ahead','air','all','allow','almost','alone','along','already','also','although','always','American','among','amount','analysis','and','animal',
         'another','answer','any','anyone','anything','appear','apply','approach','area','argue','arm','around','arrive','art','article','artist','as','ask','assume','at','attack','attention','attorney',
         'audience','author','authority','available','avoid','away','baby','back','bad','bag','ball','bank','bar','base','be','beat','beautiful','because','become','bed','before','begin','behavior','behind',
         'believe','benefit','best','better','between','beyond','big','bill','billion','bit','black','blood','blue','board','body','book','born','both','box','boy','break','bring','brother','budget','build',
         'building','business','but','buy','by','call','camera','campaign','can','cancer','candidate','capital','car','card','care','career','carry','case','catch','cause','cell','center','central','century',
         'certain','certainly','chair','challenge','chance','change','character','charge','check','child','choice','choose','church','citizen','city','civil','claim','class','clear','clearly','close','coach',
         'cold','collection','college','color','come','commercial','common','community','company','compare','computer','concern','condition','conference','Congress','consider','consumer','contain','continue',
         'control','cost','could','country','couple','course','court','cover','create','crime','cultural','culture','cup','current','customer','cut','dark','data','daughter','day','dead','deal','death','debate',
         'decade','decide','decision','deep','defense','degree','Democrat','democratic','describe','design','despite','detail','determine','develop','development','die','difference','different','difficult',
         'dinner','direction','director','discover','discuss','discussion','disease','do','doctor','dog','door','down','draw','dream','drive','drop','drug','during','each','early','east','easy','eat','economic',
         'economy','edge','education','effect','effort','eight','either','election','else','employee','end','energy','enjoy','enough','enter','entire','environment','environmental','especially','establish','even',
         'evening','event','ever','every','everybody','everyone','everything','evidence','exactly','example','executive','exist','expect','experience','expert','explain','eye','face','fact','factor','fail','fall',
         'family','far','fast','father','fear','federal','feel','feeling','few','field','fight','figure','fill','film','final','finally','financial','find','fine','finger','finish','fire','firm','first','fish',
         'five','floor','fly','focus','follow','food','foot','for','force','foreign','forget','form','former','forward','four','free','friend','from','front','full','fund','future','game','garden','gas','general',
         'generation','get','girl','give','glass','go','goal','good','government','great','green','ground','group','grow','growth','guess','gun','guy','hair','half','hand','hang','happen','happy','hard','have',
         'he','head','health','hear','heart','heat','heavy','help','her','here','herself','high','him','himself','his','history','hit','hold','home','hope','hospital','hot','hotel','hour','house','how',
         'however','huge','human','hundred','husband','idea','identify','if','image','imagine','impact','important','improve','in','include','including','increase','indeed','indicate','individual','industry',
         'information','inside','instead','institution','interest','interesting','international','interview','into','investment','involve','issue','it','item','its','itself','job','join','just','keep','key','kid',
         'kill','kind','kitchen','know','knowledge','land','language','large','last','late','later','laugh','law','lawyer','lay','lead','leader','learn','least','leave','left','leg','legal','less','let','letter',
         'level','lie','life','light','like','likely','line','list','listen','little','live','local','long','look','lose','loss','lot','love','low','machine','magazine','main','maintain','major','majority','make',
         'man','manage','management','manager','many','market','marriage','material','matter','may','maybe','me','mean','measure','media','medical','meet','meeting','member','memory','mention','message','method',
         'middle','might','military','million','mind','minute','miss','mission','model','modern','moment','money','month','more','morning','most','mother','mouth','move','movement','movie','much','music','must',
         'myself','name','nation','national','natural','nature','near','nearly','necessary','need','network','never','new','news','newspaper','next','nice','night','no','none','nor','north','not','note','nothing',
         'notice','now','number','occur','off','offer','office','officer','official','often','oil','old','on','once','one','only','onto','open','operation','opportunity','option','or','order','organization','other',
         'our','out','outside','over','own','owner','page','pain','Painting','paper','parent','part','participant','particular','particularly','partner','party','pass','past','patient','pattern','pay','peace',
         'people','per','perform','performance','perhaps','period','person','personal','phone','political','politics','poor','popular','population','position','positive','possible','power','quite','race','radio',
         'raise','range','rate','rather','reach','read','ready','real','reality','realize','really','reason','receive','recent','recently','recognize','record','red','reduce','reflect','region','relate',
         'relationship','religious','remain','remember','remove','report','represent','Republican','require','research','resource','respond','response','responsibility','run','safe','same','save','say','scene',
         'school','science','scientist','score','sea','season','seat','second','section','security','see','seek','seem','sell','send','senior','sense','series','serious','serve','service','set','seven','several',
         'shake','share','she','shoot','short','shot','should','shoulder','show','side','sign','significant','similar','simple','simply','since','sing','single','sister','sit','site','situation','six','size',
         'skill','skin','small','smile','so','social','society','soldier','some','somebody','someone','something','sometimes','speech','spend','sport','spring','staff','stage','stand','standard','star','start',
         'state','statement','station','stay','step','still','stock','stop','store','story','strategy','street','strong','structure','student','study','stuff','style','subject','success','successful','such',
         'suddenly','suffer','suggest','summer','support','sure','surface','system','table','take','talk','task','tax','teach','teacher','team','technology','television','tell','ten','tend','term','test','than',
         'thank','thing','think','third','this','those','though','thought','thousand','threat','three','through','throughout','throw','thus','time','to','today','together','tonight','too','top','total','tough',
         'toward','town','trade','traditional','training','travel','treat','treatment','tree','trial','trip','trouble','true','truth','try','turn','TV','two','type','under','understand','unit','until','up','upon',
         'us','use','usually','value','various','very','victim','view','violence','visit','voice','vote','wait','weapon','wear','week','weight','well','west','western','what','whatever','when','where','whether',
         'whose','why','wide','wife','will','win','wind','window','wish','with','within','without','woman','wonder','word','work','worker','world','worry','would','write','writer','wrong','yard','yeah','year',
         'yes','yet','you','young','your','yourself']




# -- >> SECOND WINDOWS IN WHICH MAIN APPLICATION
# - FIRST <> SECOND WINDOWS COMPLETE FUNCTION MODULE
def main():
    global score
    global miss
    global timer   
    global count
    global BGM  

    
    # WINDOWS GUI MAIN
    root= Tk()
    root.title('') # © 2022 S-ARC. All rights reserved.
    root.geometry("800x520")
    root.resizable(False, False)
    backg = "#FFFFFF"
    root.configure(background = backg)
   
    #version declared
    dec = "Version "
    ver= "1.2"
    verdec = str(dec + ver)
    
    #Release Date
    date = "26 "
    month = "June "
    year = "2022 "
    released = str(date + month + year)
    vrel = str(released)
    
    # - SECOND <> EXIT FUNCTION
    
    def Exit1x000000():
            sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent = root)
            if sure == True:
                root.destroy()
            else:
                print("CALLID - NORB0C3")
    bc00 = "WM_DELETE_WINDOW"
    root.protocol(bc00, Exit1x000000)
    
    def web_site():
        try:
            webbrowser.open("https://sarwanboi.github.io/sarwanportfolio.github.io/")
            pass
        except Exception as Err:
            messagebox.showerror("Error", Err)
    def Instagram():
        try:
            webbrowser.open("www.instagram.com/_sarwan_._")
            pass
        except Exception as Err:
            messagebox.showerror("Error", Err)
    def Github():
        try:
            webbrowser.open("https://github.com/sarwanboi")
            pass
        except Exception as Err:
            messagebox.showerror("Error", Err)     
    def Github_Soft():
        try:
            webbrowser.open("https://sarwanboi.github.io/skill_improver.github.io/v1.2/")
            pass
        except Exception as Err:
            messagebox.showerror("Error", Err)
    def  GmailLink():
        try:
            webbrowser.open("mailto:rangersarwan@gmail.com")
            pass
        except Exception as Err:
            messagebox.showerror("Error", Err)
    
    def developer():
        
        rootB= Tk()
        rootB.title('Skill Improver') # © 2022 S-ARC. All rights reserved.
        rootB.geometry("400x520")
        rootB.resizable(False, False)
        #rootB.overrideredirect(True)
        
        ###############################################################################################################################
        backg = "#FFFFFF"
        rootB.configure(background = backg)
        Devs = Frame(rootB, width=400, height=500, relief="raised",background="#FFFFFF")
        Devs.place(x= 0,y= -20)
        
        ###############################################################################################################################
        
        B00 = "#000"
        GFF = "LIGHTGREEN"
        WFF = "#FFFFFF"
        
        ###############################################################################################################################
        
        Header = Label(Devs)
        Header.configure(text="About Application",font=('Calibri (Body)', 18, 'bold'), background="#FFF",foreground="lightgreen")
        Header.place(x=40, y= 40 )
        
        ApplicationN = Label(Devs)
        ApplicationN.configure(text="Application Name: ",font=('Calibri (Body)', 9, 'bold'), background=WFF,foreground=B00)
        ApplicationN.place(x=40, y= 100)
        
        ApplicationNB = Label(Devs)
        ApplicationNB.configure(text="Skill Improver",font=('Calibri (Body)', 9, 'bold'), background=WFF,foreground=GFF)
        ApplicationNB.place(x=220, y= 100)
        
        ApplicationV = Label(Devs)
        ApplicationV.configure(text="Application Version: ",font=('Calibri (Body)', 9, 'bold'), background=WFF,foreground=B00)
        ApplicationV.place(x=40, y= 140)
        
        ApplicationVB = Label(Devs)
        ApplicationVB.configure(text=ver,font=('Calibri (Body)', 9, 'bold'), background=WFF,foreground=GFF)
        ApplicationVB.place(x=220, y= 140)
        
        ApplicationD = Label(Devs)
        ApplicationD.configure(text="Developer Name: ",font=('Calibri (Body)', 9, 'bold'), background=WFF,foreground=B00)
        ApplicationD.place(x=40, y= 180)
        
        ApplicationDB = Label(Devs)
        ApplicationDB.configure(text="Sarwan Yadav",font=('Calibri (Body)', 9, 'bold'), background=WFF,foreground=GFF)
        ApplicationDB.place(x=220, y= 180)
        
        ApplicationR = Label(Devs)
        ApplicationR.configure(text="Application Release Date :",font=('Calibri (Body)', 9, 'bold'), background=WFF,foreground=B00)
        ApplicationR.place(x=40, y= 220)
        
        ApplicationRB = Label(Devs)
        ApplicationRB.configure(text=vrel,font=('Calibri (Body)', 9, 'bold'), background=WFF,foreground=GFF)
        ApplicationRB.place(x=220, y= 220)
        
        ###############################################################################################################################
        
        HeaderB = Label(Devs)
        HeaderB.configure(text="Contact Us",font=('Calibri (Body)', 18, 'bold'), background=WFF,foreground="#1E90FF")
        HeaderB.place(x=40, y= 260 )
        
        
        
        
        ApplicationNC = Label(Devs)
        ApplicationNC.configure(text="Developer Website:",font=('Calibri (Body)', 9, 'bold'), background=WFF,foreground=B00)
        ApplicationNC.place(x=40, y= 320)
        Web = Button(Devs, command=web_site)
        Web.configure(text="Website Link", background='#fff', foreground='#1E90FF', relief='flat', activebackground='#fff',borderwidth="0", height='1', width='10',overrelief="flat", activeforeground="BLUE")
        Web.place(x=222, y= 320)
        



        ApplicationVC = Label(Devs)
        ApplicationVC.configure(text="Github:",font=('Calibri (Body)', 9, 'bold'), background=WFF,foreground=B00)
        ApplicationVC.place(x=40, y= 360)
        Webg = Button(Devs, command=Github)
        Webg.configure(text="Github Link", background='#fff', foreground='#1E90FF', relief='flat', activebackground='#fff',borderwidth="0", height='1', width='10',overrelief="flat", activeforeground="BLUE")
        Webg.place(x=220, y= 360)
        



        ApplicationNC = Label(Devs)
        ApplicationNC.configure(text="Gmail: ",font=('Calibri (Body)', 9, 'bold'), background=WFF,foreground=B00)
        ApplicationNC.place(x=40, y= 400)
        Webg2 = Button(Devs, command=GmailLink)
        Webg2.configure(text="Open Gamil", background='#fff', foreground='#1E90FF', relief='flat', activebackground='#fff',borderwidth="0", height='1', width='10',overrelief="flat", activeforeground="BLUE")
        Webg2.place(x=220, y= 400)
        



        ApplicationLC = Label(Devs)
        ApplicationLC.configure(text="Instagram: ",font=('Calibri (Body)', 9, 'bold'), background=WFF,foreground=B00)
        ApplicationLC.place(x=40, y= 440)
        WebI = Button(Devs, command=Instagram)
        WebI.configure(text="Instagram Link", background='#fff', foreground='#1E90FF', relief='flat', activebackground='#fff',borderwidth="0", height='1', width='10',overrelief="flat", activeforeground="BLUE")
        WebI.place(x=226, y= 440)
        #
        ApplicationSC = Label(Devs)
        ApplicationSC.configure(text="Download Latest Version: ",font=('Calibri (Body)', 9, 'bold'), background=WFF,foreground=B00)
        ApplicationSC.place(x=40, y= 480)
        WebS = Button(Devs, command=Github_Soft)
        WebS.configure(text="Website Link", background='#fff', foreground='#1E90FF', relief='flat', activebackground='#fff',borderwidth="0", height='1', width='10',overrelief="flat", activeforeground="BLUE")
        WebS.place(x=222, y= 480)
        ###############################################################################################################################
    def time_io():
        global timer,score,miss, second
        second = Label(frameO)
        if timer>30:
            pass
        else:
         timerlabelcount.configure(fg='orange')
        if timer>11:
            pass
        else:
            timerlabelcount.configure(fg='red')
        if timer>0:
            timer -=1
            timerlabelcount.configure(text=timer)
            timerlabelcount.after(1000,time_io)
        else:
            resul = score - miss
            if score == resul:
               startlabel.configure(text="Well Done Buddy", background=BGM)
            else:
                startlabel.configure(text="You Can Try Better", background=BGM)
                second.configure(text="Try To Reach  More Score In Less Time", foreground="ORANGE", background=BGM)
                second.place(x=30,y=100)
            timerlabelcount.configure(foreground="blue")
            finalresult.configure(text="Result Is Ready", foreground = "green")
            HL = Label(frameTH, text="Hit -",foreground="ORANGE", font=('Calibri (Body)', 9, 'italic'), background=BGM)
            ML = Label(frameTH, text="Miss -",foreground="ORANGE", font=('Calibri (Body)', 9, 'italic'), background=BGM)
            TSL = Label(frameTH, text="Final Score - ",foreground="ORANGE", font=('Calibri (Body)', 9, 'italic'), background=BGM)
            HL.place(x=90, y=70)
            ML.place(x= 90, y=90)
            TSL.place(x= 90, y=110)         
            H = Label(frameTH, text=score,foreground="GREEN", font=('Calibri (Body)', 9, 'italic'), background=BGM)
            M = Label(frameTH, text=miss,foreground="GREEN", font=('Calibri (Body)', 9, 'italic'), background=BGM)
            TS = Label(frameTH, text=score-miss,foreground="GREEN", font=('Calibri (Body)', 9, 'italic'), background=BGM)
            H.place(x= 200, y=70)
            M.place(x= 200, y=90)
            TS.place(x= 200, y=110)
            fscore = score-miss
             ## Writing result File and appending the result
            TimeVar = time.strftime("%I:%M:%S %p")
            full_date = time.localtime()
            day = str(full_date.tm_mday)
            month = str(full_date.tm_mon)
            year = str(full_date.tm_year)
            date = 'Date - ' + day + '/' + month + '/' + year + ', ' + 'Time - ' + TimeVar
            with open('Records.txt', 'a') as f:
                f.write('\nYour Result: Hit = {} | Miss = {} | Total Score = {} At {}'.format(score,miss,fscore,date)) 
            rr= messagebox.askretrycancel('Notification','Wanna Play Again!!!!') 
            if rr==True:
                H.configure(text='')
                M.configure(text='')
                TS.configure(text='')
                HL.configure(text='')
                ML.configure(text='')
                TSL.configure(text='')
                second.configure(text="")
                startlabel.configure(text='Start Typing')
                startlabel.place(x=140)
                gameinstruction.configure(text="Type the Word and hit enter button")
                finalresult.configure(text='Result Pending', foreground = "ORANGE")
                score=0
                miss=0
                timer=60
                timerlabelcount.configure(text=timer)
                wordlabel.configure(text=words[0])
                scorelabelcount.configure(text=score)
                wordentry.delete(0, END)
            else:
                def fired():
                    root.destroy()
                startlabel.configure(text="Closing App", foreground="RED", font=('Calibri (Body)', 9, 'italic'))
                second.configure(text="Closing In Five Seconds", foreground="RED", font=('Calibri (Body)', 8, 'italic'), background=BGM)
                second.place(x=90,y=100)
                startlabel.place(x=140)
                startlabel.after(5000,fired)
    def startgame(event):
        global score, miss
        if timer==60:
            time_io()
        gameinstruction.configure(text='', background=BGM)
        startlabel.configure(text='Give Your Best', background=BGM)
        startlabel.place(x=125)
        if wordentry.get()== wordlabel['text']:
            score +=1
            scorelabelcount.configure(text=score)
        else:
            miss +=1
        random.shuffle(words)
        wordlabel.configure(text=words[0])
        wordentry.delete(0,END)
    
    score=0
    miss=0
    timer=60
    count=0
    
    
    
    
    BGM = "#F0FFF0"    #F0FFF0
    BGMI = "#000000"
    BGMG = "#98FB98"
    # FRAME

    ####################
    frameO = Frame(root)
    frameT = Frame(root)
    frameTH = Frame(root)
    framefooter = Frame(root)
    frameO.config(background=BGM, width=240, height=140)
    frameT.config(background=BGM, width=200, height=100)
    frameTH.config(background=BGM, width=300, height=140)
    framefooter.config(background=BGMG, width=800, height=26)
    frameO.place(x=20,y=120)
    frameT.place(x= 10, y=320)
    frameTH.place(x=450, y=120)
    framefooter.place(x=0,y=500)
    ############################
    
    fontlabel=Label(root,text="Skill Improver",font=('Calibri (Body)', 22, 'bold'),foreground="#90EE90", background="#F0FFF0", width=18)
    fontlabel.place(x=230,y=10)
    
    wordTo = Label(frameT,text="Write this word in entry box",font=('Calibri (Body)', 9, 'bold'), foreground=BGMI, background=BGM)
    wordTo.place(x=10,y=20)
    wordlabel=Label(frameT,text=words[0],font=('Calibri (Body)', 18, 'bold'), foreground='grey', background=BGM)#87CEEB
    wordlabel.place(x= 10, y=50)
    
    scorelabel=Label(frameO,text='Your Score -',font=('Calibri (Body)', 9, 'bold'),foreground=BGMI, background=BGM)
    scorelabel.place(x=10,y=10)
    scorelabelcount=Label(frameO,text=score,font=('Calibri (Body)', 9, 'italic bold'),foreground=BGMI, background=BGM)
    scorelabelcount.place(x=200,y=10)

    timerlabel=Label(frameO,text='Time Left -',font=('Calibri (Body)', 9, 'bold'),foreground=BGMI, background=BGM)
    timerlabel.place(x=10,y=45)
    timerlabelcount=Label(frameO,text=timer,font=('Calibri (Body)', 9, 'italic bold'),foreground="BLUE", background=BGM)
    timerlabelcount.place(x=200,y=45)
    
    msg = Label(frameO,text='Message -',font=('Calibri (Body)', 9, 'bold'),foreground=BGMI, background=BGM)
    msg.place(x= 10, y= 78)
    
    startlabel=Label(frameO,text='Start Typing',font=('Calibri (Body)', 9, 'italic bold'),foreground="GREEN", background=BGM)
    startlabel.place(x=140,y=78)
    
    instructor = Label(frameTH,text='Instruction -',font=('Calibri (Body)', 9, 'bold'),foreground=BGMI, background=BGM)
    instructor.place(x= 10, y= 10)
    
    gameinstruction= Label(frameTH,text="Type the Word and hit enter button",font=('Calibri (Body)', 9, 'italic bold'),foreground='GREEN',
                           background=BGM) 
    gameinstruction.place(x=90,y= 10)
    
    result = Label(frameTH,text='Result -',font=('Calibri (Body)', 9, 'bold'),foreground=BGMI, background=BGM)
    result.place(x= 10, y= 45)
    
    finalresult = Label(frameTH,text='Pending',font=('Calibri (Body)', 9, 'bold'),foreground = "ORANGE", background=BGM)
    finalresult.place(x=90,y= 45)
    
    wordentry= Entry(root,font=('',16,'italic bold'),bd=1,justify='center', background="#EEEEEE", foreground="#C0C0C0")
    wordentry.place(x=480,y=350)
    wordentry.focus_set()
    
    copyright=Label(root,text="Skill Improver © 2022. All rights reserved.",foreground='BLACK',background=BGMG, font=('Calibri (Body)', 7,'bold'))
    copyright.place(x=580,y=500)
    
    Devs = Button(root, command= developer)
    Devs.configure(text="About Us", background="#fcfcfc", foreground='#000000', relief='flat', activebackground='orange',borderwidth="0", 
                   font=('Calibri (Body)', 7, 'bold'), height='1', width='7',overrelief="flat")
    Devs.place(x=10,y=502)
    
    root.bind('<Return>',startgame)
    root.mainloop()
       
 

def Start():
    w=Tk()

    width_of_window = 800
    height_of_window = 465
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
    w.overrideredirect(1)
    w.configure(bg="#FFF")
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground='red', background='#fff') #4f4f4f
    progress = Progressbar(w, style = "red.Horizontal.TProgressbar", orient = HORIZONTAL, length = 810, mode = 'determinate',)




    # -- >> PROGRESS BAR BACKGROUND FUNCTION
    def bar():
        l4 = Label(w)
        progress.place(x = -5,y = 457)
        def redict_open():
            w.destroy()
            st2 = main
            threading.Thread(target=st2).start()
            
        def redict_step():
            l4.configure(text = "Redirecting to your application...", foreground = "green")
            l4.after(820, redict_open)
        def redict():
            l4.configure(text="All things okay...", foreground = "green") 
            lst1=('Calibri (Body)', 7,'italic bold')
            l1.config(font = lst1)
            l4.after(460, redict_step)
        l1=Label(w,text = 'Skill Improver', foreground = 'ORANGE',background = a)
        lst1=('Calibri (Body)', 7,'bold')
        l1.config(font = lst1)
        l1.place(x = 20, y = 410)
        l4.configure(text = 'Checking...', foreground = 'black', background = "#FFF", font=('Calibri (Body)', 8,'italic'))
        l4.place(x = 20, y = 425)
        l4.after(200, redict)
        
        r=0
        for i in range(120):
            progress['value'] = r
            w.update_idletasks()
            time.sleep(0.0002)
            r = r + 1
    


    # -->> DESIGN AND POSITIONING
            
    # COMMON COLOUR        
    a = "#FFFFFF"       

    # LABELS       
    l1 = Label(w, text = 'WELCOME TO')
    l2 = Label(w, text = 'SKILL IMPROVER APPLICATION')
    l3 = Label(w, text = '"This application helps in improving your typing skills"')
    l4 = Label(w, text = 'PRACTICE  MAKES  A  PERSON  PERFECT')
    l5 = Label(w, text = 'FOUNDER  &  DEVELOPER')
    l6 = Label(w, text = 'sarwan yadav')

    # BUTTON
    b1 = Button(w, command = bar)

    # FONT
    lst1 = ('Calibri (Body)', 28, 'bold') 
    lst2 = ('Calibri (Body)', 24, 'bold')
    lst3 = ('Segoe Script',11, 'bold')
    lst4 = ('Calibri (Body)', 16, 'bold')
    lst5 = ('Calibri (Body)', 12, 'bold')
    lst6 = ('Segoe Script', 12, 'italic')
    # CONFIGURE 
    b1.configure(width = 10, height = 1, text = "Let's Go", border = 0, relief = "flat")
    b1.configure(foreground ='#000000', background='#D3D3D3', overrelief = "flat")
    l1.configure(foreground = 'ORANGE',  background = a, font = lst1)
    l2.configure(foreground = 'ORANGE',  background = a, font = lst2)
    l3.configure(foreground = '#000000', background = a, font = lst3)
    l4.configure(foreground = '#000000', background = a, font = lst4)
    l5.configure(foreground = '#000000', background = a, font = lst5)
    l6.configure(foreground = '#000000', background = a, font = lst6)

    # PLACE
    l1.place(x = 260, y = 50)
    l2.place(x = 150, y = 120)
    l3.place(x = 163, y = 170)
    l4.place(x = 175, y = 240)
    l5.place(x = 292, y = 320)
    l6.place(x = 320, y = 360)   
    b1.place(x = 685, y = 425)




    # -->> MAINLOOP
    w.mainloop()
st=Start
threading.Thread(target=st).start()
