import pandas as pd
import plotly.express as px
import collections


def negative_1_if_count_is_odd(count):
    # if this is an odd numbered entry in its bin, make its y coordinate negative
    # the y coordinate of the first entry is 0, so entries 3, 5, and 7 get
    # negative y coordinates
    if count % 2 == 1:
        return -1
    else:
        return 1


def swarm(
    X_series,
    fig_title,
    point_size=16,
    fig_width=800,
    gap_multiplier=1.2,
    bin_fraction=0.95,  # slightly undersizes the bins to avoid collisions
):
    # sorting will align columns in attractive c-shaped arcs rather than having
    # columns that vary unpredictably in the x-dimension.
    # We also exploit the fact that sorting means we see bins sequentially when
    # we add collision prevention offsets.
    X_series = X_series.copy().sort_values()

    # we need to reason in terms of the marker size that is measured in px
    # so we need to think about each x-coordinate as being a fraction of the way from the
    # minimum X value to the maximum X value
    min_x = min(X_series)
    max_x = max(X_series)

    list_of_rows = []
    # we will count the number of points in each "bin" / vertical strip of the graph
    # to be able to assign a y-coordinate that avoids overlapping
    bin_counter = collections.Counter()

    for x_val in X_series:
        # assign this x_value to bin number
        # each bin is a vertical strip slightly narrower than one marker
        bin = (((fig_width*bin_fraction*(x_val-min_x))/(max_x-min_x)) // point_size)

        # update the count of dots in that strip
        bin_counter.update([bin])

        # remember the "y-slot" which tells us the number of points in this bin and is sufficient to compute the y coordinate unless there's a collision with the point to its left
        list_of_rows.append(
            {"x": x_val, "y_slot": bin_counter[bin], "bin": bin})

    # iterate through the points and "offset" any that are colliding with a
    # point to their left apply the offsets to all subsequent points in the same bin.
    # this arranges points in an attractive swarm c-curve where the points
    # toward the edges are (weakly) further right.
    bin = 0
    offset = 0
    for row in list_of_rows:
        if bin != row["bin"]:
            # we have moved to a new bin, so we need to reset the offset
            bin = row["bin"]
            offset = 0
        # see if we need to "look left" to avoid a possible collision
        for other_row in list_of_rows:
            if (other_row["bin"] == bin-1):
                # "bubble" the entry up until we find a slot that avoids a collision
                while ((other_row["y_slot"] == row["y_slot"]+offset)
                       and (((fig_width*(row["x"]-other_row["x"]))/(max_x-min_x)
                              // point_size) < 1)):
                    offset += 1
                    # update the bin count so we know whether the number of
                    # *used* slots is even or odd
                    bin_counter.update([bin])

        row["y_slot"] += offset
        # The collision free y coordinate gives the items in a vertical bin
        # y-coordinates to evenly spread their locations above and below the
        # y-axis (we'll make a correction below to deal with even numbers of
        # entries).  For now, we'll assign 0, 1, -1, 2, -2, 3, -3 ... and so on.
        # We scale this by the point_size*gap_multiplier to get a y coordinate
        # in px.
        row["y"] = (row["y_slot"]//2) * \
            negative_1_if_count_is_odd(row["y_slot"])*point_size*gap_multiplier

    # if the number of points is even, move y-coordinates down to put an equal
    # number of entries above and below the axis
    for row in list_of_rows:
        if bin_counter[row["bin"]] % 2 == 0:
            row["y"] -= point_size*gap_multiplier/2

    df = pd.DataFrame(list_of_rows)
    # One way to make this code more flexible to e.g. handle multiple categories
    # would be to return a list of "swarmified" y coordinates here and then plot
    # outside the function.
    # That generalization would let you "swarmify" y coordinates for each
    # category and add category specific offsets to put the each category in its
    # own row

    fig = px.scatter(
        df,
        x="x",
        y="y",
        title=fig_title,
    )
    # we want to suppress the y coordinate in the hover value because the
    # y-coordinate is irrelevant/misleading
    fig.update_traces(
        marker_size=point_size,
        # suppress the y coordinate because the y-coordinate is irrelevant
        hovertemplate="<b>value</b>: %{x}",
    )
    # we have to set the width and height because we aim to avoid icon collisions
    # and we specify the icon size in the same units as the width and height
    fig.update_layout(width=fig_width, height=(
        point_size*max(bin_counter.values())+200))
    fig.update_yaxes(
        showticklabels=False,  # Turn off y-axis labels
        ticks='',               # Remove the ticks
        title=""
    )
    return fig


df = px.data.iris()  # iris is a pandas DataFrame
fig = swarm(df["sepal_length"], "Sepal length distribution from 150 iris samples")
# The iris data set entries are rounded so there are no collisions.
# a more interesting test case for collision avoidance is:
# fig = swarm(pd.Series([1, 1.5, 1.78, 1.79, 1.85, 2,
#            2, 2, 2, 3, 3, 2.05, 2.1, 2.2, 2.5, 12]))
fig.show(renderer="json")