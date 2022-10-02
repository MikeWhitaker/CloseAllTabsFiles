import sublime
import sublime_plugin

class CloseWithoutSaving(sublime_plugin.WindowCommand):
    def run(self):
        for win in sublime.windows():
            for view in win.views():
                view.window().focus_view(view)
                view.set_scratch(True);
                view.window().run_command('close_file')
