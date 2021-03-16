from datetime import datetime
import time

class Timer:
    """This class performs any operations needed with both datetime and time libraries
    """
    
    __FMT = '%H:%M:%S'
    
    def time_delta(self, time_in, time_exit):
        """This functions calculates the minutes since the hour of entrance until the hour of leaving
    
        Args:
            time_in (string): The hour when the vehicle created a ticket
            time_exit (string): The hour when the vehicle left the parking
    
        Returns:
            time: the total time that the vehicle has been parked (expressed in minutes)
        """
        delta = datetime.strptime(time_exit, self.__FMT) - datetime.strptime(time_in, self.__FMT)
        return delta.total_seconds() / 60
    
    def get_date_today(self):
        """This functions only get the today's date
    
        Returns:
            time: The today's date in format Day-Month-Year
        """
        return datetime.today().strftime('%d-%m-%Y')
