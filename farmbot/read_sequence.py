import yaml
import subscribe_to_farmbot.client as client
import subscribe_to_farmbot.my_device_id as my_device_id

class SequenceHander():
    def __init__(self,  file_name):
        self.sequences = []
        self.file = open(file_name, "r")

    def send_sequences(sequences, file_name):
        """sequences : A list of sequences, by "name", to be sent to the FarmBot
           file_name : Name of the file the YAML sequence is stored in."""
        file = open(file_name, "r")
        yaml_file = yaml.load(file)
        # Convert YAML to CeleryScript here
        for name in sequences:
            cs_obj = convert_sequence(yaml_file[name])
            client.publish("bot/" + my_device_id + "/from_clients", json_payload)

    def convert_sequence(yaml_obj):
        """yaml_obj: A YAML object representing a sequence
           returns: A CeleryScript JSON object of a sequence."""
           # This function can call itself to return well-formatted sub-sequences
