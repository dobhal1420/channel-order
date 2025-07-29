from util.source import SourceOptions

class FormInputValidator:
    @staticmethod
    def validate(file1, file2, selected_option_str):
        if not file1 or not file2:
            return False, "Please upload both files before validating.", None

        # Check file extensions
        if not file1.lower().endswith('.json'):
            return False, "File 1 must be a JSON file.", None
        if not file2.lower().endswith('.csv'):
            return False, "File 2 must be a CSV file.", None

        try:
            channel_source = SourceOptions(selected_option_str)
        except ValueError:
            return False, "Invalid channel source selected.", None

        return True, "", channel_source