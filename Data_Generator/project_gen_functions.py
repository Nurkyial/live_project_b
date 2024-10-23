import random
from faker import Faker
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

fake = Faker()


def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))


start_date = datetime.now() - timedelta(days=365)
end_date = datetime.now()


def probability_value(start, end, probability):
    return start if random.random() < probability else end
