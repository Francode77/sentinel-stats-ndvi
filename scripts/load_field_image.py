from sentinelhub import (
    CRS,
    BBox,
    DataCollection,
    Geometry,
    SentinelHubStatistical,
    SentinelHubStatisticalDownloadClient,
    SHConfig,
    parse_time,
    bbox_to_dimensions,
     
    DownloadRequest,
    MimeType,
    MosaickingOrder,
    SentinelHubDownloadClient,
    SentinelHubRequest,  
)
import matplotlib.pyplot as plt
import geopandas as gpd    
from datetime import datetime,timedelta


df_agri = gpd.read_file("./data/processed/agri_region_utm31.shp") 

# Function to return the dates for the sentinelhub request
def get_interval(date_str):
 
    date_format = '%Y-%m-%d'

    interval_from = datetime.strptime(date_str, date_format)
    interval_to = interval_from+timedelta(days=1) 

    # the date can be formatted as a string if needed
    date_A = interval_from.strftime('%Y-%m-%d')
    date_B = interval_to.strftime('%Y-%m-%d')
    return date_A, date_B


class Field:
    def __init__(self, id):
        self.df = df_agri
        self.id = id

    def geometry(self):
        self.result=self.df[self.df['UIDN'] == self.id]['geometry'].values
        return self.result
    
    def bounding_box(self):
        field_bbox=self.geometry().total_bounds
 
        field_bbox[0]=field_bbox[0]-200
        field_bbox[1]=field_bbox[1]-100
        field_bbox[2]=field_bbox[2]+200
        field_bbox[3]=field_bbox[3]+200
        return field_bbox
    
    def get_id(self):
        return self.id
 
def load_field_image(field_id,date_str):

    config = SHConfig('francode-profile')

    if not config.sh_client_id or not config.sh_client_secret:
        print("Warning! To use Statistical API, please provide the credentials (OAuth client ID and client secret).")
    # Get the interval dates 
    date_A,date_B=get_interval(date_str)
    # Get the bounding box of field_id
    field = Field(field_id) 
    field_bbox=field.bounding_box()

    # Calculate the BBox and dimensions
    min_x, min_y, max_x, max_y=field_bbox
    resolution=10
    field_bbox = BBox(bbox=(min_x, min_y, max_x, max_y), crs=CRS.UTM_31N)
    field_size = bbox_to_dimensions(field_bbox, resolution=resolution)

    evalscript_true_color = """
        //VERSION=3

        function setup() {
            return {
                input: [{
                    bands: ["B02", "B03", "B04"]
                }],
                output: {
                    bands: 3 
                }
            };
        }

        function evaluatePixel(sample) {
            return [sample.B04, sample.B03, sample.B02];
        }
    """


    request_true_color = SentinelHubRequest(
        data_folder=f"./data/sentinel2/fields/{field_id}/",
        evalscript=evalscript_true_color,
        input_data=[
            SentinelHubRequest.input_data(
                data_collection=DataCollection.SENTINEL2_L1C,
                time_interval=(f"{date_A}T00:00:00", f"{date_B}T00:00:00"), 
            )
        ],
        responses=[SentinelHubRequest.output_response("default", MimeType.TIFF)],
        bbox=field_bbox,
        size=field_size,
        config=config,
    )

    true_color_img = request_true_color.get_data(save_data=True)

    true_color_img  = request_true_color.get_data()

    image = true_color_img[0]

    
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_aspect('equal')
    plt.imshow(image*4)
    #show(rgb_composite_raw, transform=img_meta['transform'], ax=ax, alpha=0.88 )
    #ax = df_field.plot(ax=ax, alpha=0.272, edgecolor='k') 
    
    ax.set_title(f"Field {field_id} (UTM31 / EPSG:32631)")
    plt.show()