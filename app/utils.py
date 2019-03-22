import base64
import json
import os
import re
import time
from datetime import datetime

import pytz
from django.utils import dateparse
from django.utils import timezone, timesince

from app import settings


class Utils(object):
    # Operators
    HTML_TAG_STATUS_ACTIVE_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_ACTIVE_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Active <b></div>'
    HTML_TAG_STATUS_INACTIVE_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_INACTIVE_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Inactive <b></div>'
    HTML_TAG_STATUS_BLOCKED_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_BLOCKED_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Blocked <b></div>'
    HTML_TAG_STATUS_UNVERIFIED_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_UNVERIFIED_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Unverified <b></div>'
    HTML_TAG_STATUS_UNAPPROVED_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_UNAPPROVED_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Unapproved <b></div>'

    # Orders
    HTML_TAG_ORDER_STATUS_PENDING = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_RED + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Pending <b></div>'
    HTML_TAG_ORDER_STATUS_REQUESTED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_BLUE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Requested <b></div>'
    HTML_TAG_ORDER_STATUS_LEVEL0_APPROVED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_ORANGE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Level Approved  <b></div>'
    HTML_TAG_ORDER_STATUS_LEVEL1_APPROVED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_ORANGE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Level-1 Approved  <b></div>'
    HTML_TAG_ORDER_STATUS_LEVEL2_APPROVED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_ORANGE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Level-2 Approved  <b></div>'
    HTML_TAG_ORDER_STATUS_LEVEL3_APPROVED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_ORANGE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Level-3 Approved  <b></div>'
    HTML_TAG_ORDER_STATUS_LEVEL4_APPROVED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_ORANGE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Level-4 Approved  <b></div>'
    HTML_TAG_ORDER_STATUS_LEVEL5_APPROVED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_ORANGE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Level-5 Approved  <b></div>'
    HTML_TAG_ORDER_STATUS_LEVEL6_APPROVED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_ORANGE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Level-6 Approved  <b></div>'
    HTML_TAG_ORDER_STATUS_LEVEL1_REJECTED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_DARK_GREY + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Level-1 Rejected  <b></div>'
    HTML_TAG_ORDER_STATUS_LEVEL2_REJECTED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_DARK_GREY + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Level-2 Rejected <b></div>'
    HTML_TAG_ORDER_STATUS_LEVEL3_REJECTED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_DARK_GREY + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Level-3 Rejected <b></div>'
    HTML_TAG_ORDER_STATUS_LEVEL4_REJECTED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_DARK_GREY + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Level-4 Rejected <b></div>'
    HTML_TAG_ORDER_STATUS_LEVEL5_REJECTED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_DARK_GREY + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Level-5 Rejected <b></div>'
    HTML_TAG_ORDER_STATUS_LEVEL6_REJECTED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_DARK_GREY + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Level-6 Rejected <b></div>'
    HTML_TAG_ORDER_STATUS_REVIEWED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_BLUE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Reviewed <b></div>'
    HTML_TAG_ORDER_STATUS_APPROVED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_ORANGE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Approved <b></div>'
    HTML_TAG_ORDER_STATUS_REJECTED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_DARK_GREY + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Rejected <b></div>'
    HTML_TAG_ORDER_STATUS_ASSIGNED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_BLUE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Assigned <b></div>'
    HTML_TAG_ORDER_STATUS_SUPPLIER_SELECTED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_BLUE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Vendor Category Selected <b></div>'
    HTML_TAG_ORDER_STATUS_PROPOSAL_GENERATED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_BLUE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Proposal Generated <b></div>'
    HTML_TAG_ORDER_STATUS_PROPOSAL_REQUESTED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_BLUE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Proposal Requested <b></div>'
    HTML_TAG_ORDER_STATUS_PROPOSAL_EVALUATED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_BLUE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Proposal Evaluated <b></div>'
    HTML_TAG_ORDER_STATUS_PROPOSAL_APPROVED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_ORANGE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Proposal Approved <b></div>'
    HTML_TAG_ORDER_STATUS_PROPOSAL_REJECTED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_DARK_GREY + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Proposal Rejected  <b></div>'
    HTML_TAG_ORDER_STATUS_PURCHASE_GENERATED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_BLUE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Purchase Generated <b></div>'
    HTML_TAG_ORDER_STATUS_PROPOSAL_ACKNOWLEDGED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_BLUE + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Proposal Acknowledged <b></div>'
    HTML_TAG_ORDER_STATUS_RECEIVED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_GREEN + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Received <b></div>'
    HTML_TAG_ORDER_STATUS_PARTIALLY_PAID = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_GREEN + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Partially Paid <b></div>'
    HTML_TAG_ORDER_STATUS_PAID = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_GREEN + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Paid <b></div>'
    HTML_TAG_ORDER_STATUS_CLOSED = '<div class=\'center-block\' style=\'background-color:' + settings.COLOR_DARK_GREY + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Closed <b></div>'

    # Notifications
    HTML_TAG_STATUS_UNREAD_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_BLOCKED_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Pending <b></div>'
    HTML_TAG_STATUS_READ_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_UNAPPROVED_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Unresolved <b></div>'
    HTML_TAG_STATUS_FIXED_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_ACTIVE_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Fixed <b></div>'

    @staticmethod
    def format_device_date(value):
        index1 = -1
        index2 = -1
        index = -1
        counter = 0
        for c in value:
            index = index + 1
            # print(c)
            if c == '/':
                counter = counter + 1
                if counter == 1:
                    index1 = index
                if counter == 2:
                    index2 = index

        # print(index1)
        # print(index2)

        date = value[0: index1]
        # print('Date: %s', date)
        month = value[index1 + 1: index2]
        # print('Month: %s', month)
        year = value[index2 + 1: len(value)]
        # print('Year: %s', year)

        if int(date) < 10:
            str_date = '0' + date
        else:
            str_date = '' + date
        if int(month) < 10:
            str_month = '0' + month
        else:
            str_month = '' + month
        if int(year) < 10:
            str_year = '000' + year
        elif int(year) < 100:
            str_year = '00' + year
        elif int(year) < 1000:
            str_year = '0' + year
        else:
            str_year = '' + year

        value = str_year + '-' + str_month + '-' + str_date
        print(value)
        return value

    @staticmethod
    def format_device_time(value):
        index1 = -1
        index2 = -1
        index = -1
        counter = 0
        for c in value:
            index = index + 1
            # print(c)
            if c == ':':
                counter = counter + 1
                if counter == 1:
                    index1 = index
                if counter == 2:
                    index2 = index

        # print(index1)
        # print(index2)

        hours = value[0: index1]
        # print('Hours: %s', hours)
        minutes = value[index1 + 1: index2]
        # print('Minutes: %s', minutes)
        seconds = value[index2 + 1: len(value)]
        # print('Seconds: %s', seconds)

        if int(hours) < 10:
            str_hours = '0' + hours
        else:
            str_hours = '' + hours
        if int(minutes) < 10:
            str_minutes = '0' + minutes
        else:
            str_minutes = '' + minutes
        if int(seconds) < 10:
            str_seconds = '0' + seconds
        else:
            str_seconds = '' + seconds

        value = str_hours + ':' + str_minutes + ':' + str_seconds
        print(value)
        return value

    @staticmethod
    def convert_string_to_datetime(value):
        value = datetime.strptime(value, settings.APP_CONSTANT_INPUT_DATETIME_FORMAT)
        return value

    @staticmethod
    def get_epochtime_ms():
        return round(datetime.utcnow().timestamp() * 1000)

    @staticmethod
    def get_current_datetime_utc():
        return datetime.now(tz=timezone.utc).strftime(settings.APP_CONSTANT_INPUT_DATETIME_FORMAT)

    @staticmethod
    def get_convert_datetime(value, tz_from, tz_to):
        value = datetime.strftime(value, settings.APP_CONSTANT_INPUT_DATETIME_FORMAT)
        value = dateparse.parse_datetime(value)
        utc_dt = pytz.timezone(str(tz_from)).localize(value)
        display_dt = utc_dt.astimezone(pytz.timezone(str(tz_to)))
        return str(datetime.strftime(display_dt, settings.APP_CONSTANT_DISPLAY_DATETIME_FORMAT))

    @staticmethod
    def get_convert_datetime_in_milliseconds(value, tz_from, tz_to):
        value = datetime.strftime(value, settings.APP_CONSTANT_INPUT_DATETIME_FORMAT)
        value = dateparse.parse_datetime(value)
        utc_dt = pytz.timezone(str(tz_from)).localize(value)
        display_dt = utc_dt.astimezone(pytz.timezone(str(tz_to)))
        display_dt = datetime.strftime(display_dt, settings.APP_CONSTANT_DISPLAY_DATETIME_FORMAT)
        d = datetime.strptime(display_dt, settings.APP_CONSTANT_DISPLAY_DATETIME_FORMAT)
        return int(time.mktime(d.timetuple()))

    # refer http://strftime.org/
    @staticmethod
    def get_format_input_date(value):
        value = datetime.strptime(value, '%d %b %Y').strftime('%Y-%m-%d')
        return value

    @staticmethod
    def get_format_display_date(value):
        value = datetime.strptime(value, '%Y-%m-%d').strftime('%d %b %Y')
        return value

    @staticmethod
    def get_fuse_format_date(value):
        value = datetime.strptime(value, '%Y-%m-%d').strftime('%Y-%m-%d')
        return value

    # noinspection PyShadowingNames
    @staticmethod
    def pretty_date(time=False):
        """
        Get a datetime object or a int() Epoch timestamp and return a
        pretty string like 'an hour ago', 'Yesterday', '3 months ago',
        'just now', etc
        """
        now = datetime.now()
        if type(time) is int:
            diff = now - datetime.fromtimestamp(time)
        elif isinstance(time, datetime):
            diff = now - time
        elif not time:
            diff = now - now
        else:
            diff = now - now
        second_diff = diff.seconds
        day_diff = diff.days

        if day_diff < 0:
            return ''

        if day_diff == 0:
            if second_diff < 10:
                return "just now"
            if second_diff < 60:
                return str(int(round(second_diff, 0))) + " seconds ago"
            if second_diff < 120:
                return "a minute ago"
            if second_diff < 3600:
                return str(int(round(second_diff / 60, 0))) + " minutes ago"
            if second_diff < 7200:
                return "an hour ago"
            if second_diff < 86400:
                return str(int(round(second_diff / 3600, 0))) + " hours ago"
        if day_diff == 1:
            return "Yesterday"
        if day_diff < 7:
            return str(int(round(day_diff, 0))) + " days ago"
        if day_diff < 31:
            return str(int(round(day_diff / 7, 0))) + " weeks ago"
        if day_diff < 365:
            return str(int(round(day_diff / 30, 0))) + " months ago"
        return str(int(round(day_diff / 365, 0))) + " years ago"

    @staticmethod
    def bytes_2_human_readable(number_of_bytes):
        if number_of_bytes < 0:
            raise ValueError("!!! number_of_bytes can't be smaller than 0 !!!")

        step_to_greater_unit = 1024.

        number_of_bytes = float(number_of_bytes)
        unit = 'bytes'

        if (number_of_bytes / step_to_greater_unit) >= 1:
            number_of_bytes /= step_to_greater_unit
            unit = 'KB'

        if (number_of_bytes / step_to_greater_unit) >= 1:
            number_of_bytes /= step_to_greater_unit
            unit = 'MB'

        if (number_of_bytes / step_to_greater_unit) >= 1:
            number_of_bytes /= step_to_greater_unit
            unit = 'GB'

        if (number_of_bytes / step_to_greater_unit) >= 1:
            number_of_bytes /= step_to_greater_unit
            unit = 'TB'

        precision = 1
        number_of_bytes = round(number_of_bytes, precision)

        return str(number_of_bytes) + ' ' + unit

    @staticmethod
    def save_file_by_bytes(file_data_in_bytes, file_path):
        f = open(file_path, 'wb')
        f.write(file_data_in_bytes)
        f.close()

    # noinspection PyUnusedLocal
    @staticmethod
    def save_image_base64(image_data, file_path):
        format, file_string = image_data.split(';base64,')
        # print("format", format)
        ext = format.split('/')[-1]
        # print("file_string", file_string)
        # print("ext", ext)
        file_bytes = base64.b64decode(file_string)
        # print("file_bytes", file_bytes)
        f = open(file_path, 'wb')
        f.write(file_bytes)
        f.close()

    @staticmethod
    def delete_file(path):
        """ Deletes file from filesystem. """
        if os.path.isfile(path):
            os.remove(path)

    @staticmethod
    def get_ip_address(request):
        # request.environ['REMOTE_ADDR']
        # request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        return request.environ['REMOTE_ADDR']

    @staticmethod
    def get_browser_details_from_request(request):
        return 'Browser:' + request.user_agent.browser.family + ' ' + request.user_agent.browser.version_string \
               + ' Device:' + request.user_agent.device.family \
               + ' OS:' + request.user_agent.os.family + ' ' + request.user_agent.os.version_string

    @staticmethod
    def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv / 3], 16) for i in range(0, lv, lv / 3))

    @staticmethod
    def rgb_to_hex(rgb):
        return '#%02x%02x%02x' % rgb

    @staticmethod
    def is_json(data):
        try:
            json.loads(data)
        except ValueError:
            return False
        return True

    @staticmethod
    def is_json_or_xml(data):
        # Remove tabs, spaces, and new lines when reading
        data = re.sub(r'\s+', '', data)
        if re.match(r'^({|[).+(}|])$', data):
            return 1
        if re.match(r'^<.+>$', data):
            return 2
        return 0

    @staticmethod
    def timesince(timestamp):
        """Convert a timestamp to human readable time since"""

        mapping = {'minute': 'min',
                   'hour': 'hr',
                   'week': 'wk',
                   'month': 'mo',
                   'year': 'yr'}

        if timestamp is None:
            return "Never"

        text = timesince.timesince(timestamp)
        for key in mapping.keys():
            text = text.replace(key, mapping[key])

        return text


class FileObject:
    name = ''

    def __init__(self, name):
        self.name = name
