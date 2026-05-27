# Submitting Extinct Glacier Data to GLIMS

## Background

GLIMS (Global Land Ice Measurements from Space) tracks glaciers that have disappeared by marking their status as `gone` in the GLIMS Glacier Database. This capability was added in 2023 in recognition of the growing number of glaciers that have completely melted away or shrunk to the point that local experts no longer consider them glaciers.

A glacier is considered extinct when it has completely melted away, or shrunk to the extent that it is no longer recognized as a glacier by regional experts. This includes glaciers that have become small ice patches below the size threshold used by national inventories, as well as those that have fully disappeared. The final determination of extinction is left to local and regional experts.

GLIMS is primarily interested in glaciers that have disappeared within the last 50–100 years — those that are victims of more recent changes to climate, rather than glaciers lost since the Little Ice Age. Submissions from the community are actively welcomed to make the record more complete.

When GLIMS data are downloaded, extinct glaciers have a value of `gone` in the `glacier_status` (or `glac_stat`) field, enabling analysis of trends across geographic regions.

## Before You Submit

The glaciers you are reporting must already have records in the GLIMS Glacier Database — that is, they must have been mapped and contributed to GLIMS at some point in the past, and therefore have a GLIMS glacier ID. If you have outlines of glaciers that are not yet in the database, please contact the GLIMS team before submitting extinction data.

If you are unsure whether a glacier has an existing record, you can look up GLIMS glacier IDs using the [GLIMS Glacier Viewer](https://www.glims.org/maps/glims) or the [GLIMS Text Search Interface](https://www.glims.org/maps/gmng).

## Required Information

For each glacier you are reporting as extinct, you will need the following:

**GLIMS Glacier ID** — The unique identifier assigned to the glacier in the GLIMS database (e.g., `G006813E46133N`). IDs follow the format `G` + 6-digit longitude + `E`/`W` + 5-digit latitude + `N`/`S`.

**Estimated disappearance date** (`est_disappear_date`) — Your best estimate of when the glacier disappeared, in ISO 8601 format (`YYYY-MM-DD`). The day and month may be approximate; for example, if only the year is known, use `YYYY-01-01` and set a large uncertainty.

**Date uncertainty** (`est_disappear_unc`) — The uncertainty in the disappearance date, expressed as an integer number of days.

**Source** (`gone_source`) — Attribution for the disappearance determination. This should include the name of the person who made the determination, their institution, and/or a relevant publication DOI or image ID. For example: `Jane Doe (University of X), Landsat 8 image LC08_L1TP_XYZ_20200901` or `Doe et al. 2023, https://doi.org/10.xxxx/xxxxx`.

**Date added to GLIMS** (`glims_added_extinct_date`) — The date on which you are submitting this information (`YYYY-MM-DD`). If left blank, today's date will be used.

## How to Submit

Extinct glacier submissions are handled through the GLIMS submissions GitHub repository using an issue form.

1. Navigate to the [glims-submissions repository](https://github.com/glims-nsidc/glims-submissions/issues)and click **New Issue**.
2. Select the **Extinct Glacier** template.
3. Fill in the title with a brief description, for example: `Extinct glacier: North Cascade glaciers, USA`.
4. Enter your glacier IDs in the **Glacier IDs** field — one ID per line. For larger submissions, you may attach a `.txt`, `.csv`, or `.xlsx` file instead of pasting IDs directly. If providing a file, place glacier IDs in the first column with no header row.
5. Complete the remaining metadata fields.
6. Click **Submit new issue**.

Submissions from multiple glaciers may be grouped into a single issue if they share the same disappearance date, uncertainty, and source. If different glaciers have different metadata, open a separate issue for each group.

## Grouping Submissions

All glaciers listed in a single issue will be assigned the same `est_disappear_date`, `est_disappear_unc`, and `gone_source`. If the glaciers you are reporting disappeared at different times or were documented from different sources, please open a separate issue for each group.

## After Submission

Once you submit the issue it will be reviewed by GLIMS staff at NSIDC. You may be contacted with questions before the data are ingested. The `glacier_status` field for each glacier will be updated to `gone` in the database after review, and the records will be visible in the GLIMS Glacier Viewer under the extinct glaciers layer.

## Questions

For general questions about extinct glacier submissions or the GLIMS database, see the [GLIMS guide on extinct glaciers](https://www.glims.org/MapsAndDocs/extinct_glaciers_guide.html) or contact the GLIMS team via a github issue or emailing nsidc@nsidc.org. 
