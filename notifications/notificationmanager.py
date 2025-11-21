import platform

Class NotificationManager:
    def __init__(self, timer_minutes):
        if platform.system() == 'Windows':
            self.notifier = WindowsNotifier(timer_minutes)
        elif platform.system() == 'Linux':
            self.notifier = LinuxNotifier(timer_minutes)
        elif platform.system() == 'Darwin':
            self.notifier = MacOSNotifier(timer_minutes)
        else:
            self.notifier = GenericOSNotifier(timer_minutes)
            
    def show(self, message):
        self.notifier.show(message)
        
