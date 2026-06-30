# Submitting Extinct Glaciers to GLIMS

## Background

GLIMS (Global Land Ice Measurements from Space) tracks glaciers that have disappeared by marking their status as gone in the GLIMS Glacier Database. This capability was added in 2023 in recognition of the growing number of glaciers that have completely melted away or shrunk to the point that local experts no longer consider them glaciers.

A glacier is considered extinct when local or regional experts determine that the glacier can no longer be identified or considered as a glacier.  This determination can be made based on direct observations in the field or based on remotely sensed imagery.  
For a glacier to be designated extinct in the GLIMS Glacier Database, an outline and glacier-id for the glacier must exist in the database.  
The following cases are examples and not an exhaustive list.

* A glacier has completely melted away;
* The area of glacier ice is smaller than generally considered to be a glacier (e.g. )
* Glacial ice is debris covered and is dead ice (e.g. )
* Glacier ice can no longer be seen by experts on high resolution imagery
* The area of glacier ice is less than the threshold set by a national inventory

GLIMS is primarily interested in glaciers that have disappeared within the last 50–100 years, rather than glaciers lost since the Little Ice Age. When GLIMS data are downloaded, extinct glaciers have a value of gone in the glacier_status (or glac_stat) field, enabling analysis of trends across geographic regions.


## Before Submitting 

The NSIDC DAAC welcomes extinct glacier submissions from the community to make glacier outline records more complete.
First determine if the extinct glacier or glaciers is in the GLIMS Glacier Database.

To determine if a glacier is in the GLIMS Glacier Database, use theGLIMS Glacier Viewer](https://www.glims.org/maps/glims) or the [GLIMS Text Search Interface](https://www.glims.org/maps/gmng).  These tools will also provide the GLIMS glacier ID for the glacier.

If you have outlines for glaciers that are not in the database, please submit these using the [new submission form](https://github.com/glims-nsidc/glims-submissions/issues).


## Required Information

For each glacier you are reporting as extinct, you will need the following:

**GLIMS Glacier ID** — The unique identifier assigned to the glacier in the GLIMS database (e.g., `G006813E46133N`). IDs follow the format `G` + 6-digit longitude + `E`/`W` + 5-digit latitude + `N`/`S`.

**Estimated disappearance date** (`est_disappear_date`) — Your best estimate of when the glacier disappeared, in ISO 8601 format (`YYYY-MM-DD`).  The date of disappearance should be the date that the glacier was observed to be gone in the field, or the date of the image that was used to determine it was gone.

**Date uncertainty** (`est_disappear_unc`) — The uncertainty in the disappearance date, expressed as an integer number of days.

**Source** (`gone_source`) — Attribution for the disappearance determination. This should include the name of the person who made the determination, their institution, and/or a relevant publication DOI or image ID. For example: `Jane Doe (University of X), Landsat 8 image LC08_L1TP_XYZ_20200901` or `Doe et al. 2023, https://doi.org/10.xxxx/xxxxx`.

**Date added to GLIMS** (`glims_added_extinct_date`) — The date on which you are submitting this information (`YYYY-MM-DD`). If left blank, today's date will be used.

## How to Submit

Extinct glacier submissions are handled through the GLIMS submissions GitHub repository using an issue form.

1. Navigate to the [glims-submissions repository](https://github.com/glims-nsidc/glims-submissions/issues)
2. Click **New Issue**.
3. Select the **Extinct Glacier** template.
4. Fill in the title with the region where this glacier is, for example: `Extinct glacier: North Cascade glaciers, USA`. 
5. Enter your glacier IDs in the **Glacier IDs** field — one ID per line. For larger submissions, you may attach a `.txt`, `.csv`, or `.xlsx` file instead of pasting IDs directly. If providing a file, place glacier IDs in the first column with no header row.
6. Complete the remaining fields in the form.
7. Click **Submit new issue**.

Submissions from multiple glaciers may be grouped into a single issue if they share the same disappearance date, uncertainty, and source. If different glaciers have different metadata, open a separate issue for each group.

## Grouping Submissions

All glaciers listed in a single issue will be assigned the same `est_disappear_date`, `est_disappear_unc`, and `gone_source`. If the glaciers you are reporting disappeared at different times or were documented from different sources, please open a separate issue for each group.

## After Submission

Once submitted the issue will be reviewed by the NSIDC DAAC team . You may be contacted with questions before the data are ingested. Once reviewed, the `glacier_status` field for each glacier will be updated to `gone` in the Glacier Database, and the records will be visible in the GLIMS Glacier Viewer under the extinct glaciers layer.


## Questions

For questions, please contact  NSIDC User Services at nsidc@nsidc.org. 

## References
Pope, A. (2025). Glacier or not? The importance of nuance in definitions of vanishing glaciers. Annals of Glaciology, 66, e32. https://doi.org/10.1017/aog.2025.10030

Raup, B. H., Andreassen, L. M., Boyer, D., Howe, C., Pelto, M., & Rabatel, A. (2025). Tracking extinct glaciers in GLIMS. Annals of Glaciology, 66, e35. https://doi.org/10.1017/aog.2025.10027

Linsbauer, A., Huss, M., Hodel, E., Bauder, A., & Barandun, M. (2025). Vanished glaciers of the Swiss Alps: An inventory-based assessment from 1973 to 2016. Annals of Glaciology, 66, e33. https://doi.org/10.1017/aog.2025.10031

