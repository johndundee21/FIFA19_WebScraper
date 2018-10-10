import re as StringManipulation

class String:
    @staticmethod
    def FormatToExcel(String):
         return StringManipulation.sub(r"(?<=\w)([A-Z])", r" \1", "".join(String.split()))