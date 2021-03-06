

import urllib2
import json
import operator

DATA = [
    "https://data.cityofnewyork.us/resource/jt7v-77mi.json",
    "https://data.cityofnewyork.us/resource/kiv2-tbus.json"
    ]

# some errors in dates exist in the files - earliest year available
EARLIEST_YEAR = 2013


# http://www1.nyc.gov/site/finance/vehicles/services-violation-codes.page
VIOLATION = list(range(0,100))
VIOLATION[0] = ""
VIOLATION[1] = ""
VIOLATION[2] = ""
VIOLATION[3] = ""
VIOLATION[4] = "No parking - Metered Bus Only"
VIOLATION[5] = "Failure to make a right turn from bus lane"
VIOLATION[6] = "Parking tractor-trailer on residential street between 9PM and 5AM"
VIOLATION[7] = "Red Light Camera"
VIOLATION[8] = "Blocking an intersection"
VIOLATION[9] = "Vehicle idling in a restricted area"
VIOLATION[10] = "No Parking (check this one) ****************************"
VIOLATION[11] = "No Standing - Hotel Loading/Unloading"
VIOLATION[12] = "No Standing - Snow Emergency"
VIOLATION[13] = "No Standing - Taxi Stand"
VIOLATION[14] = "No Standing"
VIOLATION[15] = "Other"
VIOLATION[16] = "No Standing - Commercial Vehicles Only"
VIOLATION[17] = "No Standing - Authorized Vehicles Only"
VIOLATION[18] = "No Standing - Bus Lane"
VIOLATION[19] = "No Standing - Bus Stop"
VIOLATION[20] = "No Parking"
VIOLATION[21] = "No Parking - Street Cleaning (Alternate Side Parking)"
VIOLATION[22] = "No Parking - Hotel Loading/Unloading"
VIOLATION[23] = "No Parking - Taxi Stand"
VIOLATION[24] = "No Parking - Authorized Vehicles Only"
VIOLATION[25] = "No Standing - Commuter Van Stop"
VIOLATION[26] = "No Standing - For-Hire Vehicles Only"
VIOLATION[27] = "Handicap Parking Only"
VIOLATION[28] = "Diplomat Overtime Parking"
VIOLATION[29] = "Altering intercity bus permit"
VIOLATION[30] = "Stopping or standing in assigned intercity bus stop while not loading"
VIOLATION[31] = "No Standing - Commercial Vehicles Only"
VIOLATION[32] = "Parking at a broken meter for longer than maximum time"
VIOLATION[33] = "\"Feeding Meter\" - Parking in metered spot for longer than maximum time"
VIOLATION[34] = "Expired Meter"
VIOLATION[35] = "Parking in metered spot to sell goods"
VIOLATION[36] = "Speed Camera"
VIOLATION[37] = "Parking at meter for longer than maximum time"
VIOLATION[38] = "Failing to display munimeter tag on windshield"
VIOLATION[39] = "Parking for longer than maximum time"
VIOLATION[40] = "Parking at Fire Hydrant"
VIOLATION[41] = "Other"
VIOLATION[42] = "Commercial - Expired Meter"
VIOLATION[43] = "Commercial - Expired Meter"
VIOLATION[44] = "Commercial - Parking at meter for longer than maximum time"
VIOLATION[45] = "Parking too far from curb"
VIOLATION[46] = "Double Parking"
VIOLATION[47] = "Double Parking"
VIOLATION[48] = "Parking in bike lane"
VIOLATION[49] = "No Parking - Construction Zone"
VIOLATION[50] = "Parking in crosswalk"
VIOLATION[51] = "Parking on sidewalk"
VIOLATION[52] = "Parking in internsection"
VIOLATION[53] = "Parking in a safety zone"
VIOLATION[54] = "Other"
VIOLATION[55] = "Parking in a tunnel or on a highway"
VIOLATION[56] = "Parking along barrier or divided highway"
VIOLATION[57] = "No Parking" # Blue Zone
VIOLATION[58] = "No Parking" # Marginal street or waterfront
VIOLATION[59] = "Improper parking angle"
VIOLATION[60] = "Improper parking angle"
VIOLATION[61] = "Improper parking angle or facing wrong direction"
VIOLATION[62] = "Not parked properly within marked parking spot"
VIOLATION[63] = "Parking in a park at night"
VIOLATION[64] = "No Standing - Diplomats Only"
VIOLATION[65] = "Diplomat Overtime Parking"
VIOLATION[66] = "Parking a trailer not attached to a motor vehicle"
VIOLATION[67] = "Parking in front of pedestrian ramp"
VIOLATION[68] = "Not parking as marked on posted sign"
VIOLATION[69] = "Commercial - Failing to display munimeter tag on windshield"
VIOLATION[70] = "Expired Registration Sticker"
VIOLATION[71] = "Expired Inspection Sticker"
VIOLATION[72] = "(NY Plates Only) Damaged or fake inspection certificate"
VIOLATION[73] = "Expired, damaged, void, fake, or incorrect registration sticker"
VIOLATION[74] = "Missing License Plate"
VIOLATION[75] = "License plate doesn't match registration sticker"
VIOLATION[76] = "Other"
VIOLATION[77] = "Parking a bus"
VIOLATION[78] = "Parking commercial vehicle on residential street between 9PM and 5AM"
VIOLATION[79] = "Bus - Standing at curb"
VIOLATION[80] = "Missing/Broken lights"
VIOLATION[81] = "No Standing - Diplomats Only"
VIOLATION[82] = "Improper Commercial Vehicle"
VIOLATION[83] = "Vehicle Not Registered"
VIOLATION[84] = "Commercial - Vehicle lift in down position when nobody is with vehicle"
VIOLATION[85] = "Commercial - Parking for more than 3 hours"
VIOLATION[86] = "Commercial - Parking for more than 3 hours" # 14-60 sts, 1-8 avs
VIOLATION[87] = "Other"
VIOLATION[88] = "Other"
VIOLATION[89] = "No Parking" # Garment District
VIOLATION[90] = "Other"
VIOLATION[91] = "Parking in order to sell a vehicle by a person who regularly sells vehicles"
VIOLATION[92] = "Parking in order to wash or repair vehicle by a person who regularly does so"
VIOLATION[93] = "Illegal parking to change a flat tired"
VIOLATION[94] = "Vehicle Release penalty associated with NYPD'S Violation Tow Program"
VIOLATION[95] = "Other"
VIOLATION[96] = "Parking within 50 feet of railroad crossing"
VIOLATION[97] = "Parking on vacant lot"
VIOLATION[98] = "Parking in front of driveway"
VIOLATION[99] = "Other"


FINE = list(range(0,100))
FINE[0] = -1
FINE[1] = 515
FINE[2] = 515
FINE[3] = 515
FINE[4] = 115
FINE[5] = 115
FINE[6] = 265
FINE[7] = 50
FINE[8] = 115
FINE[9] = 115
FINE[10] = 115
FINE[11] = 115
FINE[12] = 95
FINE[13] = 115
FINE[14] = 115
FINE[15] = -1
FINE[16] = 95
FINE[17] = 95
FINE[18] = 115
FINE[19] = 115
FINE[20] = 65
FINE[21] = 65
FINE[22] = 60
FINE[23] = 65
FINE[24] = 65
FINE[25] = 115
FINE[26] = 115
FINE[27] = 180
FINE[28] = 95
FINE[29] = 515
FINE[30] = 515
FINE[31] = 115
FINE[32] = 65
FINE[33] = 65
FINE[34] = 65
FINE[35] = 65
FINE[36] = 50
FINE[37] = 65
FINE[38] = 65
FINE[39] = 65
FINE[40] = 115
FINE[41] = -1
FINE[42] = 65
FINE[43] = 65
FINE[44] = 65
FINE[45] = 115
FINE[46] = 115
FINE[47] = 115
FINE[48] = 115
FINE[49] = 95
FINE[50] = 115
FINE[51] = 115
FINE[52] = 115
FINE[53] = 115
FINE[54] = -1
FINE[55] = 115
FINE[56] = 115
FINE[57] = 65
FINE[58] = 65
FINE[59] = 115
FINE[60] = 65
FINE[61] = 65
FINE[62] = 65
FINE[63] = 95
FINE[64] = 95
FINE[65] = 95
FINE[66] = 65
FINE[67] = 165
FINE[68] = 65
FINE[69] = 65
FINE[70] = 65
FINE[71] = 65
FINE[72] = 65
FINE[73] = 65
FINE[74] = 65
FINE[75] = 65
FINE[76] = -1
FINE[77] = 65
FINE[78] = 65
FINE[79] = 115
FINE[80] = 60
FINE[81] = 95
FINE[82] = 115
FINE[83] = 65
FINE[84] = 65
FINE[85] = 65
FINE[86] = 115
FINE[87] = -1
FINE[88] = -1
FINE[89] = 115
FINE[90] = -1
FINE[91] = 65
FINE[92] = 65
FINE[93] = 65
FINE[94] = 100
FINE[95] = -1
FINE[96] = 95
FINE[97] = 65
FINE[98] = 95
FINE[99] = 0




def format_time(time):
    if len(time) != 5:
        return False

    r = time[0] + time[1] + ':' + time[2] + time[3]
    if time[4] == "A":
        r += " AM"
    else:
        r += " PM"

    return r



def search_plate(plate):
    r = ""
    
    info = []
    
    for x in DATA:

        # load all violations
        result = json.loads(urllib2.urlopen(x + "?plate_id=" + plate).read())
        
        # insert each violation into main violation array
        for res in result:

            # sometimes there are duplicate results - make sure to only output once
            unique = True
            for check in info:
                if res["summons_number"] == check["summons_number"]:
                    unique = False
                    break

            if unique:

                res["sort_time"] = res["violation_time"]

                # this is necessary so that it sorts by time properly (AM/PM issue)
                if "P" in res["sort_time"]:
                    res["sort_time"] = "9"+res["sort_time"]

                info.append(res)

    print len(info)


    # convert JSON data to HTML
    total_fines = 0
    count = 1
    for row in sorted(info, key=operator.itemgetter("issue_date","sort_time"), reverse=True): # sort


        # date
        dsplit = row["issue_date"].split('T')[0].split('-')
        if int(dsplit[0]) < EARLIEST_YEAR:
            date = "Unknown"
        else:
            date = dsplit[1] + '/' + dsplit[2] + '/' + dsplit[0]


        # time
        time = format_time(row["violation_time"])


        # violation name
        violation_name = VIOLATION[int(row["violation_code"])]

        
        # violation fine
        fine = FINE[int(row["violation_code"])]

        if fine < 0:
            violation_fine = "Unknown"
        else:
            total_fines += fine
            violation_fine = "$"+str(fine)


        # borough
        if "violation_county" not in row.keys():
            borough = "Not Specified"
        elif row["violation_county"] == "NY":
            borough = "Manhattan"
        elif row["violation_county"] == "Q":
            borough = "Queens"
        elif row["violation_county"] == "K":
            borough = "Brooklyn"
        elif row["violation_county"] == "BX":
            borough = "The Bronx"
        elif row["violation_county"] == "R":
            borough = "Staten Island"
        else:
            borough = "Not Specified"

    
        # location
        if "street_name" in row.keys():
            if "house_number" in row.keys():
                location = row["house_number"] + ' ' + row["street_name"]
            elif "intersecting_street" in row.keys():
                location = row["street_name"] + " & " + row["intersecting_street"]
            else:
                location = row["street_name"]
        else:
            location = "Unknown"



    
        # SPECIAL CASES - extras

        # do not include additional info for these codes
        exempt_codes = [1,2,3,5,6,7,8,9,27,29,30,36,40,41,45,46,47,50,51,52,53,54,55,56,59,60,61,62,66,67,68,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,86,87,88,90,91,92,93,94,95,96,97,98,99]
#        exempt_codes = [19,40,46,47,67,77,78]            
                         


        # munimeter over time
        additional = ""
        if "time_first_observed" in row.keys() and int(row["violation_code"]) not in exempt_codes:
            expired = format_time(row["time_first_observed"])
            if expired != False:
                additional += "Meter expired at " + expired


#        elif "from_hours_in_effect" in row.keys() and "to_hours_in_effect" in row.keys() and int(row["violation_code"]) not in exempt_codes:
        elif "days_parking_in_effect" in row.keys() and int(row["violation_code"]) not in exempt_codes:



            # Only display days if no parking/standing zone 
            display_days = True
            if row["violation_code"] == "38":
                display_days = False
                additional += "Metered Parking "
            elif "No Standing" in violation_name:
                additional += "No Standing "
            else:
                additional += "No Parking "

            
            # No Parking Anytime
            if "from_hours_in_effect" not in row.keys() or row["from_hours_in_effect"] == "ALL":
                additional += "Anytime"
                display_days = False
            else:

                from_hours = format_time(row["from_hours_in_effect"])
                to_hours = format_time(row["to_hours_in_effect"])

                # if either is not in proper time format, don't display any info
                if from_hours != False and to_hours != False:
                    additional += from_hours + " - " + to_hours
                else:
                    additional = ""
                    display_days = False


            if display_days:
                days = row["days_parking_in_effect"]
                if days == "YYYYYYY":
                    additional += " All Days"
                elif days == "YYYYYYB" or days == "YYYYYY":
                    additional += " Except Sunday"
                elif days == "YYYYYBB" or days == "YYYYY":
                    additional += ", Monday - Friday"
                else:
                    additional += ","
                    if len(days) > 0 and days[0] == "Y":
                        additional += " Monday"
                    if len(days) > 1 and days[1] == "Y":
                        additional += " Tuesday"
                    if len(days) > 2 and days[2] == "Y":
                        additional += " Wednesday"
                    if len(days) > 3 and days[3] == "Y":
                        additional += " Thursday"
                    if len(days) > 4 and days[4] == "Y":
                        additional += " Friday"
                    if len(days) > 5 and days[5] == "Y":
                        additional += " Saturday"
                    if len(days) > 6 and days[6] == "Y":
                        additional += " Sunday"


                # if days[0] == "Y":
                #     additional += " Monday"
                # if days[1] == "Y":
                #     additional += " Tuesday"
                # if days[2] == "Y":
                #     additional += " Wednesday"
                # if days[3] == "Y":
                #     additional += " Thursday"
                # if days[4] == "Y":
                #     additional += " Friday"
                # if days[5] == "Y":
                #     additional += " Saturday"
                # if days[6] == "Y":
                #     additional += " Sunday"
                
        if additional != "":
            violation_name += """<div class="desc">%s</div>"""%additional


        date += """<div class="desc">%s</div>"""%row["summons_number"]

        r += """
<tr>
<td class="num">%(count)d</td>
<td class="date">%(date)s</td>
<td class="time">%(time)s</td>
<td class="violation">%(violation_name)s</td>
<td class="borough">%(borough)s</td>
<td class="location">%(location)s</td>
<td class="fine">%(violation_fine)s</td>
</tr>"""%{"count":count, "date":date, "time":time, "violation_name":violation_name, "borough":borough, "location":location, "violation_fine":violation_fine}
        count += 1

    return {"violation_table":r, "total_fines":total_fines}

