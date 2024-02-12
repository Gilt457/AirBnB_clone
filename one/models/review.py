#!/usr/bin/python3
"""Module for Review class"""

import models.base_model as bm


class Review(bm.BaseModel):
    """Class to handle review data"""

    text = ""
    user_id = ""
    place_id = ""
