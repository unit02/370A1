# A1 for COMPSCI340/SOFTENG370 2015
# Prepared by Robert Sheehan
# Modified by ...

# You are not allowed to use any sleep calls.

from threading import Lock, Event
from process import State
import threading

class Dispatcher():
    """The dispatcher."""

    MAX_PROCESSES = 8

    def __init__(self):
        """Construct the dispatcher."""
        self.processList = []
        self.topOfStack = 0

    def set_io_sys(self, io_sys):
        """Set the io subsystem."""
        self.io_sys = io_sys

    def add_process(self, process):
        """Add and start the process."""
        # ...
        process.state = State.runnable
        process.iosys.allocate_window_to_process(process, self.topOfStack)
        self.processList.append(process)
        self.topOfStack =  self.topOfStack + 1
        process.event.set()
        process.start()

        if len(self.processList) >= 2:
            for x in range(len(self.processList) - 2):
             self.processList[x].event.clear()
        else:
            for x in range(len(self.processList) - 1):
             self.processList[x].event.clear()



    def dispatch_next_process(self):
        """Dispatch the process at the top of the stack."""
        # ...
        nextProc =  self.processList[self.topOfStack]
        nextProc.event.set()
        nextProc.start()

        if len(self.processList) > 2:
            for x in range(len(self.processList) - 2):
             self.processList[x].event.clear()
        else:
            for x in range(len(self.processList) - 1):
             self.processList[x].event.clear()



    def to_top(self, process):
        """Move the process to the top of the stack."""
        # ...


    def pause_system(self):
        """Pause the currently running process.
        As long as the dispatcher doesn't dispatch another process this
        effectively pauses the system.
        """
        # ...
        for x in range(len(self.processList)):
            self.processList[x].event.clear()

    def resume_system(self):
        """Resume running the system."""
        # ...
        self.processList[self.topOfStack-1].event.set()
        if self.topOfStack >= 2:
            self.processList[self.topOfStack -2].event.set()



    def wait_until_finished(self):
        """Hang around until all runnable processes are finished."""
        # ...


    def proc_finished(self, process):
        """Receive notification that "proc" has finished.
        Only called from running processes.
        """
        # ...
        #chekc if the top of the stack, else move to the top of the stack

        if (len(self.processList) >= 2) & (process.id != self.processList[self.topOfStack-1].id) :
            temp = self.processList[self.topOfStack - 1]
            self.io_sys.move_process(process,self.topOfStack-1)
            self.io_sys.move_process(temp,self.topOfStack -2)

        self.io_sys.remove_window_from_process(process)
        self.processList.remove(process)
        self.topOfStack = self.topOfStack-1

        if(len(self.processList)-1 >= 0):
         self.processList[len(self.processList)-1].event.set()
         if (len(self.processList) > 2):
            self.processList[len(self.processList)-2].event.set()



    def proc_waiting(self, process):
        """Receive notification that process is waiting for input."""
        # ...

    def process_with_id(self, id):
        """Return the process with the id."""
        # ...
        for i in range(len(self.processList)):
          if(id == self.processList[i].id):
                retProcess = self.processList[i]
        return retProcess
