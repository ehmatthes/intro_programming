#!/bin/bash

# This script builds the entire html page.
#  Assumes need to build from basic html, and construct
#  custom-defined pages.


# Build basic pages.
source create_common_html.sh
wait


# Modify html
source modify_custom_html.sh

printf "\n\n"
