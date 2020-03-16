
class MeetingSlot:
    """
    Class for keeping information about one meeting request
    """

    def __init__(self, user_id, submittion_time, start_meeting, end_meeting):
        """
        Contructor for setting all member variables
        """
        self.user_id = user_id
        self.submittion_time = submittion_time
        self.start_meeting = start_meeting
        self.end_meeting = end_meeting

    def is_valid(self, valid_start_time, valid_end_time):
        """
        Checks if requested meeting within valid working times

        :param valid_start_time: valid start time
        :param valid_end_time: valid end time
        """
        if self.start_meeting.time() < valid_start_time or self.end_meeting.time() > valid_end_time:
            return False

        return True

    def __repr__(self):
        """
        Impleted for debug purposes, to be able to pring MeetingSlot object
        """

        current_start_time = self.start_meeting.strftime("%Y-%m-%d %H:%M")
        current_end_time = self.end_meeting.strftime("%Y-%m-%d %H:%M")
        return f"{self.user_id} [{self.submittion_time}] [{current_start_time}] [{current_end_time}]"
