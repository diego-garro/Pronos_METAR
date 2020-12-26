from metar import Metar

obs = Metar.Metar("METAR MROC 071200Z 10018KT 3000 R07/P2000N BR VV003 17/09 A2994 RESHRA NOSIG", year=2005, month=1)
# print(obs.string())
# print(obs.dewpt, type(obs.dewpt), obs.dewpt.value())
# print(obs.press, type(obs.press), obs.press.value())
# print(obs.time, type(obs.time), obs.time.year, obs.time.month, obs.time.day, obs.time.hour)
# print(obs.wind_speed.value())
# print(obs.wind_dir.value())
# # print(obs.wind_gust.value())
# print(obs.wind_dir_to)
# print(obs.weather)
# print(obs.sky)
# print(obs.vis.value())
print(obs.time.year, obs.time.month, obs.time.day)
# print(obs.get_wind_dir())
print(obs.sky)
if obs.vis is not None:
	print(obs.vis.value())
print(obs.weather)
print(obs.runway)
print(obs.recent)
# print(obs.get_sky_conditions())