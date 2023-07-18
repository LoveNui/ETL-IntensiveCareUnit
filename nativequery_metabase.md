## Metabase Queries for MongoDB Data Retrieval

In Metabase, we have crafted some native queries to extract specific data from our MongoDB database. These queries are designed to retrieve valuable information related to patient vitals from different beds in the ICU.

### Query 1: Retrieve Blood Pressure Diastolic for Bed B001

This query focuses on fetching the latest blood pressure diastolic reading for the patient in Bed B001. It performs the following steps:

1.  **$match**: Filters the data to include only records with "bed_id" equal to "B001" (Bed B001).
2.  **$sort**: Sorts the filtered data in descending order based on the "timestamp" field, ensuring we get the latest record first.
3.  **$limit**: Limits the result to only one record, i.e., the most recent entry for Bed B001.
4.  **$project**: Projects the result, excluding the default MongoDB "_id" field and renaming the "bp_diastolic" field to "blood pressure diastolic".

    [
    
    {
    "$match": {
    "bed_id": "B001"
    }
    },
    {
    "$sort": {
    "timestamp": -1
    }
    },
    {
    "$limit": 1
    },
    {
    "$project": {
    "_id": 0,
    "bp_diastolic": "$bp_diastolic"
    }
    }
    ]

### Query 2: Retrieve Oxygen Level for Bed B002

This query focuses on obtaining the latest oxygen level reading for the patient in Bed B002. It follows the same steps as Query 1, but with the appropriate field and bed_id:

1.  **$match**: Filters the data to include only records with "bed_id" equal to "B002" (Bed B002).
2.  **$sort**: Sorts the filtered data in descending order based on the "timestamp" field, ensuring we get the latest record first.
3.  **$limit**: Limits the result to only one record, i.e., the most recent entry for Bed B002.
4.  **$project**: Projects the result, excluding the default MongoDB "_id" field and renaming the "oxygen_level" field to "oxygen level".

  

    [
    
    {
    
    "$match": {
    
    "bed_id": "B002"
    
    }
    
    },
    
    {
    
    "$sort": {
    
    "timestamp": -1
    
    }
    
    },
    
    {
    
    "$limit": 1
    
    },
    
    {
    
    "$project": {
    
    "_id": 0,
    
    "oxygen_level": "$oxygen_level"
    
    }
    
    }
    
    ]

### Query 3: Retrieve Temperature for Bed B001

This query is similar to the first two, but it focuses on retrieving the latest temperature reading for the patient in Bed B001:

1.  **$match**: Filters the data to include only records with "bed_id" equal to "B001" (Bed B001).
2.  **$sort**: Sorts the filtered data in descending order based on the "timestamp" field, ensuring we get the latest record first.
3.  **$limit**: Limits the result to only one record, i.e., the most recent entry for Bed B001.
4.  **$project**: Projects the result, excluding the default MongoDB "_id" field and renaming the "temperature" field to "temperature".

    [
    
    {
    
    "$match": {
    
    "bed_id": "B001"
    
    }
    
    },
    
    {
    
    "$sort": {
    
    "timestamp": -1
    
    }
    
    },
    
    {
    
    "$limit": 1
    
    },
    
    {
    
    "$project": {
    
    "_id": 0,
    
    "temperature": "$temperature"
    
    }
    
    }
    
    ]

These Metabase native queries allow us to quickly retrieve specific data points from MongoDB, enabling us to monitor and analyze patient vitals in real-time. The combination of Metabase and MongoDB provides us with valuable insights for better patient care and management in the ICU.
