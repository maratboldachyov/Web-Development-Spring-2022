def sleep_in(weekday, vacation):
  if not weekday and vacation or not weekday and not vacation or weekday and vacation:
    return True
  elif weekday and not vacation:
    return False
