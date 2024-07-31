from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
PATH = "API (D_33)/quizler_app/images"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")  
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_txt = self.canvas.create_text(150, 125, 
                                                    width=260,
                                                    text="Some Question Text",
                                                    fill=THEME_COLOR,
                                                    font=("Arial", 20, "italic"))
        
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file= PATH + "/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file= PATH + "/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_txt, text=q_text)

        else:
            self.canvas.itemconfig(self.question_txt, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def false_pressed(self):    
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
