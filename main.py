from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from datetime import datetime
from database import TaskDatabase

class TaskCard(BoxLayout):
    text = ""
    reminder = ""

class ToDoApp(App):
    def build(self):
        self.db = TaskDatabase()
        self.root = Builder.load_file('todo.kv')

        # Load sounds
        self.sound_add = SoundLoader.load("sounds/add.wav")
        self.sound_done = SoundLoader.load("sounds/done.wav")
        self.sound_reminder = SoundLoader.load("sounds/reminder.wav")

        # Load existing tasks
        self.load_tasks()

        # Check reminders every 30 seconds
        Clock.schedule_interval(self.check_reminders, 30)
        return self.root

    def load_tasks(self):
        task_list = self.root.ids.task_list
        task_list.clear_widgets()
        for title, completed, reminder in self.db.get_tasks():
            icon = "✅ " if completed else "🕓 "
            task_list.add_widget(TaskCard(text=icon + title, reminder=reminder))

    def add_task(self):
        task_input = self.root.ids.task_input
        reminder_input = self.root.ids.reminder_input
        title = task_input.text.strip()
        reminder = reminder_input.text.strip()

        if not title:
            return

        self.db.add_task(title, reminder if reminder else None)
        task_input.text = ""
        reminder_input.text = ""

        if self.sound_add:
            self.sound_add.play()

        self.load_tasks()

    def remove_task(self, title):
        # title comes with an icon prefix like "🕓 My Task"
        self.db.delete_task(title[2:])
        self.load_tasks()

    def complete_task(self, title):
        self.db.mark_complete(title[2:])
        if self.sound_done:
            self.sound_done.play()
        self.load_tasks()

    def delete_all(self):
        self.db.delete_all()
        self.load_tasks()

    def show_popup(self, task_title):
        box = BoxLayout(orientation='vertical', padding=15, spacing=15)

        # Animated bell image (images/bell.gif)
        bell = Image(source="images/bell.gif", anim_delay=0.1, size_hint_y=None, height=100)

        label = Label(
            text=f"⏰ Reminder!\n{task_title}",
            font_size=22,
            color=(0, 0, 0, 1),
            bold=True
        )

        btn_done = Button(
            text="✅ Mark as Done",
            size_hint_y=None,
            height=50,
            background_normal='',
            background_color=(0, 0.7, 0.3, 1)
        )
        btn_close = Button(
            text="❌ Close",
            size_hint_y=None,
            height=50,
            background_normal='',
            background_color=(1, 0.5, 0.2, 1)
        )

        box.add_widget(bell)
        box.add_widget(label)
        box.add_widget(btn_done)
        box.add_widget(btn_close)

        popup = Popup(
            title="Task Reminder 🔔",
            content=box,
            size_hint=(0.8, 0.6),
            background_color=(1, 0.9, 0.6, 1),
            auto_dismiss=False
        )

        btn_done.bind(on_release=lambda *a: (self.complete_task("🕓 " + task_title), popup.dismiss()))
        btn_close.bind(on_release=popup.dismiss)

        popup.open()

    def check_reminders(self, dt):
        now = datetime.now().strftime("%H:%M")
        for title, _, reminder in self.db.get_tasks():
            if reminder and reminder == now:
                if self.sound_reminder:
                    self.sound_reminder.play()
                self.show_popup(title)

if __name__ == '__main__':
    ToDoApp().run()
