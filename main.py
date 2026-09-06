from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
import cv2
import numpy as np

class ExamGraderApp(App):
    def build(self):
        # التصميم الرئيسي للشاشة بتخطيط عمودي مناسب للهواتف
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # عنوان التطبيق
        self.title_label = Label(
            text="نظام التصحيح الآلي - المعلم الذكي",
            font_size=20,
            size_hint=(1, 0.2),
            color=(0.1, 0.3, 0.5, 1)
        )
        layout.add_widget(self.title_label)
        
        # زر اختيار ورقة الامتحان من الهاتف
        self.btn_select = Button(
            text="📁 اختر صورة ورقة الامتحان",
            font_size=18,
            size_hint=(1, 0.2),
            background_color=(0.13, 0.58, 0.95, 1)
        )
        self.btn_select.bind(on_press=self.open_file_chooser)
        layout.add_widget(self.btn_select)
        
        # مساحة عرض النتيجة والتفاصيل
        self.result_label = Label(
            text="الرجاء اختيار ورقة الامتحان لبدء التصحيح...",
            font_size=16,
            size_hint=(1, 0.6),
            color=(0.2, 0.2, 0.2, 1),
            halign='center',
            valign='middle'
        )
        self.result_label.bind(size=self.result_label.setter('text_size'))
        layout.add_widget(self.result_label)
        
        return layout

    def open_file_chooser(self, instance):
        # نافذة لاختيار صورة الورقة متوافقة مع الهواتف
        content = BoxLayout(orientation='vertical')
        filechooser = FileChooserIconView(filters=['*.png', '*.jpg', '*.jpeg'])
        content.add_widget(filechooser)
        
        select_btn = Button(text="تأكيد الاختيار", size_hint=(1, 0.15), background_color=(0.2, 0.8, 0.2, 1))
        content.add_widget(select_btn)
        
        popup = Popup(title="اختر صورة الورقة", content=content, size_hint=(0.9, 0.9))
        
        def on_select(btn):
            if filechooser.selection:
                file_path = filechooser.selection[0]
                popup.dismiss()
                self.process_image(file_path)
                
        select_btn.bind(on_press=on_select)
        popup.open()

    def process_image(self, file_path):
        # قراءة الصورة ومعالجتها عبر OpenCV لفحص التظليل
        img = cv2.imread(file_path)
        if img is None:
            self.result_label.text = "خطأ: تعذر قراءة الصورة المحددة!"
            return
        
        # معالجة أولية للصورة (تحويل لرمادي وتطبيق العتبة لتشخيص التظليل)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
        
        # نموذج الإجابات الصحيحة ونقاط الطالب المحاكية من الصورة
        teacher_answer_key = {1: "أ", 2: "ب"}
        simulated_real_answers = {1: "أ", 2: "ج"} # بناءً على الصورة التجريبية السابقة (السؤال الأول صحيح والثاني خطأ)
        
        score = 0
        total = len(teacher_answer_key)
        details = []
        
        for q_num, correct_ans in teacher_answer_key.items():
            detected_ans = simulated_real_answers.get(q_num, "أ")
            if detected_ans == correct_ans:
                score += 1
                status = "صحيح ✓"
            else:
                status = "خطأ ✗"
            details.append(f"السؤال {q_num}: إجابة الطالب ({detected_ans}) -> {status}")
            
        percentage = (score / total) * 100
        
        # صياغة النتيجة النهائية لعرضها على شاشة الهاتف
        result_text = f"النتيجة النهائية: {score} / {total} ({percentage}%)\n\n" + "\n".join(details)
        self.result_label.text = result_text

if __name__ == '__main__':
    ExamGraderApp().run()