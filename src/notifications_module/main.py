from notifications_module.data_retrieval import get_next_liverpool_match
from notifications_module.messages import next_liverpool_pl_match_message
from common.utils import get_absolute_path, send_notification

pl_schedule_relative_path = "output/output_pl_2026_clean.json"
pl_schedule_absolute_path = get_absolute_path(pl_schedule_relative_path)

next_pl_match = get_next_liverpool_match(pl_schedule_absolute_path)

if next_pl_match is not None:

	message = next_liverpool_pl_match_message(next_pl_match)

	send_notification("Liverpool's Next Fixture", message)
else:
	send_notification("","No upcoming Liverpool fixtures found")
