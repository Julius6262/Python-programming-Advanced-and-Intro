class WeatherStation:

    def __init__(self, st_name: str):
        self._st_name = st_name
        self._obs_list = []

    def add_observation(self, observation: str):
        if len(observation) > 0:
            self._obs_list.append(observation)
        

    def latest_observation(self):
        if len(self._obs_list) > 0:
            return self._obs_list[-1]
        else:
            return ""

    def number_of_observations(self):
        return len(self._obs_list)

    def __str__(self):
        return f"{self._st_name}, {len(self._obs_list)} observations"
