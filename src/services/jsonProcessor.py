import json


class JSONProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def __enter__(self):
        try:
            self.json_pre_sort_channel_dict = {}
            with open(self.file_path, "r") as jsonfile:
                json_presort_data_list = json.load(jsonfile)

                # Extract Name and Rank from JSON to dict
                for json_presort_data in json_presort_data_list:
                    channel_name = json_presort_data['name']
                    channel_rank = json_presort_data['rank']
                    if channel_name in self.json_pre_sort_channel_dict:
                        print(
                            f"Duplicate channel name in JSON. Please upload the correct JSON with unique channels - {channel_name}"
                        )
                    else:
                        self.json_pre_sort_channel_dict[channel_name] = channel_rank

            return self.json_pre_sort_channel_dict
        except Exception as e:
            raise Exception(f"Error processing Pre-sort file: {str(e)}")

    def __exit__(self, exc_type, exc_value, traceback):
        pass
