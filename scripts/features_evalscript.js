//VERSION=3


// Normalised Difference Snow Index
// Source: https://earth.esa.int/web/sentinel/technical-guides/sentinel-2-msi/level-2a/algorithm
// values above 0.42 are usually snow

let viz = new Identity();


function setup() {
  return {
    input: [{
      bands: ["B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B8A", "B09", "B11", "B12", "CLM", "CLP", "dataMask"],
      units: "DN"
    }],
    output: [
      {
        id: "bands",
        bands: ["B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B8A", "B09", "B11", "B12"],
        sampleType: "UINT16"
      },
      {
        id: "masks",
        bands: ["CLM"],
        sampleType: "UINT16"
      },
      {
        id: "indices",
        bands: ["NDVI", "NDVI_RE1", "NBSI", "CLP" ,"NDSI"],
        sampleType: "UINT16"
      },
      {
        id: "dataMask",
        bands: 1
      }]
  }
}

function evaluatePixel(samples) {
    // Normalised Difference Vegetation Index and variation
    let NDVI = index(samples.B08, samples.B04);
    let NDVI_RE1 = index(samples.B08, samples.B05);
    
    // Normalised Difference Snow Index
    let val = index(samples.B03, samples.B11);
 
    // Bare Soil Index
    let NBSI = index((samples.B11 + samples.B04), (samples.B08 + samples.B02));

    // cloud probability normalized to interval [0, 1]
    let CLP = samples.CLP / 255.0;

    // masking cloudy pixels
    let combinedMask = samples.dataMask
    if (samples.CLM > 0) {
        combinedMask = 0;
    }

    const f = 5000;
    return {
        bands: [samples.B01, samples.B02, samples.B03, samples.B04, samples.B05, samples.B06,
                samples.B07, samples.B08, samples.B8A, samples.B09, samples.B11, samples.B12],
        masks: [samples.CLM],
        indices: [toUINT(NDVI, f), toUINT(NDVI_RE1, f), toUINT(NBSI, f), toUINT(CLP, f), toUINT(viz.process(val), f)],
        dataMask: [combinedMask]        
    };
}

function toUINT(product, constant){
  // Clamp the output to [-1, 10] and convert it to a UINT16
  // value that can be converted back to float later.
  if (product < -1) {
    product = -1;
  } else if (product > 10) {
    product = 10;
  }
  return Math.round(product * constant) + constant;
}