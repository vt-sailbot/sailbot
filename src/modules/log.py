#!/usr/bin/python
import logging, modules.utils, curses

class WebSocketLogger(logging.Handler):

    """
    A handler class which allows the cursor to stay on
    one line for selected messages
    """

    def __init__(self, listener):
        super().__init__()
        self.listener = listener

    def emit(self, record):
        try:
            packet = {'category': 'log', 'message': self.format(record), 'type': record.levelno}
            self.listener.send_data(modules.utils.getJSON(packet))
            self.flush()
        except NameError:
            print('The server thread has not been created yet. Dropping log output.')
        except:
            self.handleError(record)

class CursesHandler(logging.Handler):
    def __init__(self, screen):
        logging.Handler.__init__(self)
        self.screen = screen

        curses.start_color()
        curses.use_default_colors()
        for i in range(0, curses.COLORS):
            curses.init_pair(i + 1, i, -1)

    def emit(self, record):
        try:
            msg = self.format(record)
            screen = self.screen
            fs = "\n%s"
            
            try:

                ufs = u'\n%s'
                try:
                    screen.addstr(ufs % msg, self.get_color_pair(record.levelno))
                    screen.refresh()
                except UnicodeEncodeError:
                    screen.addstr((ufs % msg).encode(code))
                    screen.refresh()

            except UnicodeError:
                screen.addstr(fs % msg.encode("UTF-8"))
                screen.refresh()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def get_color_pair(self, level):
        index = str(level)
        #20 : 28
        return curses.color_pair({'10': 83, '20': 39, '30':  245, '40': 167, '50': 197}[index])
