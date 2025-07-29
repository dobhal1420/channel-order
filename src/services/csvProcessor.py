import pandas as pd
from util.source import  SourceOptions, SourceMappings


class CSVProcessor:
    def __init__(self, channel_source: SourceOptions, file_path: str):
        self.file_path = file_path
        self.channel_source = channel_source

    def __enter__(self):
        try:
            self.sorted_channel_data_tv_db_objects = []
            with open(self.file_path, "r", encoding="utf-8", errors="replace") as csvfile:
                # Read TV DB File
                data = pd.read_csv(csvfile, encoding="utf-8", engine="python")

                # Filter based on channel type
                condition = data['type'].isin(SourceMappings.SOURCE_MAPPING[self.channel_source])
                filtered_data = data[condition]

                # Sort by LCN
                sorted_channel_data_tv_db_dataframe = filtered_data.sort_values(by="display_number", ascending=True)

                # Convert DataFrame to list of objects
                self.sorted_channel_data_tv_db_objects = sorted_channel_data_tv_db_dataframe.to_dict(orient='records')

            return self.sorted_channel_data_tv_db_objects
        except Exception as e:
            raise Exception(f"Error processing CSV file: {str(e)}")

    def __exit__(self, exc_type, exc_value, traceback):
        pass