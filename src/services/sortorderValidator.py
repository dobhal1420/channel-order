from services.csvProcessor import CSVProcessor
from services.jsonProcessor import JSONProcessor
from util.source import SourceOptions


class SortOrderValidator:
    def __init__(self, channel_source: SourceOptions, tv_db_file: str, presort_file: str):
        self.tv_db_file = tv_db_file
        self.presort_file = presort_file
        self.channel_source = channel_source

    # Pre-processing uploaded files
    def validate(self):
        sorted_channel_data_tv_db_objects = {}
        try:
            with CSVProcessor(self.channel_source, self.tv_db_file) as csv_data:
                sorted_channel_data_tv_db_objects = csv_data
        except Exception as e:
            raise Exception(f"Error processing TV DB file: {str(e)}")

        json_pre_sort_channel_dict = {}
        try:
            with JSONProcessor(self.presort_file) as presort_data:
                json_pre_sort_channel_dict = presort_data
        except Exception as e:
            raise Exception(f"Error processing Pre-sort file: {str(e)}")

        print(json_pre_sort_channel_dict)

        # Verify TV DB data is in accordance with pre-sort JSON file
        json_prev_channel_rank = 0
        overflow_channel_data_list = []
        comparison_result = []
        is_channel_in_presort = None

        for channel_tv_db in sorted_channel_data_tv_db_objects:
            channel_name_tv_db = str(channel_tv_db['display_name'])
            channel_number_tv_db = int(channel_tv_db['display_number'])

            json_current_pointer_rank = json_pre_sort_channel_dict.get(channel_name_tv_db)
            if json_current_pointer_rank is not None:
                if json_current_pointer_rank > json_prev_channel_rank:
                    json_prev_channel_rank = json_current_pointer_rank
                    if is_channel_in_presort is None or is_channel_in_presort:
                        is_channel_in_presort = True
                    else:
                        previous_lcn = channel_number_tv_db - 1
                        message = (
                            f"Summary: Wrong Sort Order. Details: Presort channel {channel_name_tv_db} at LCN "
                            f"{channel_number_tv_db} is appearing after non-presort/overflow channel. Check channel at LCN {previous_lcn}"
                        )
                        print(message)
                        comparison_result.append(message)
                        break
                else:
                    message = (
                        f"Summary: Channel Order Mismatch. Details: {channel_name_tv_db} is placed at LCN {channel_number_tv_db}"
                    )
                    print(message)
                    comparison_result.append(message)
            else:
                is_channel_in_presort = False
                print(
                    f"Overflow Area - Channel {channel_name_tv_db} at LCN {channel_number_tv_db} does not exist in presort json file"
                )
                overflow_channel_data_list.append(channel_tv_db)

            if len(comparison_result) == 0:
                return True, "LCN order for pre-sort channels on TV matches perfectly with pre-sort file"
            else:
                errors = "\n".join(comparison_result)
                return False, f"Validation Failed:\n{errors}"