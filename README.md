# Lithograph - the website

*This website was created for by the Lithograph team at the [Agile/OGA Hackathon](https://events.agilescientific.com/event/oga-lon-hackathon) in London (23-25 November 2018)*

---
We trained two rock classification models and created a tool that allows users to upload and classify their own las file. Please check [the data preparation and training repository](https://github.com/roliveira/lithograph) if you're interested in our methodology.

### Data
We used 8 wells from the Poseidon survey (credits mentioned on our website). We quality controlled and filtered the petrophysical suite of logs down to: Gamma-Ray, Bulk-Density, Compressional Velocity, Neutron Porosity, Photoelectric Absorption, and Deep/Medium-Resistivity. We then manually labelled  the lithology log based on the composite logs (pdf files) for the training. 

### Models
We trained two models: a gradient boosting algorithm (XGBoost) and a bi-directional LSTM. The latter is the deep learning approach for which we adapted a network which was used for linguistic translation. This model would account for typical spatial/temporal geological sequences. 

### Website
We implemented the trained models in a Flask web app where users are introduced with our project and then invite to upload their own .las file for classification. The plots are Bokeh interactive log displays where you can use synchronized zooming for inspect. 

#### note: 
A reduced version of the website can be found [here](https://lithograph.pythonanywhere.com/). This does not include the LSTM model because the necessary python library is too large for the (free) hosting space on pythonanywhere.com. Check [this link](https://lithograph.pythonanywhere.com/classify-Pharos_1.las#logdisplay) if you want to see a (working) classified las file without uploading your own. Uploading your own might not work because for now the tool requires the log names to be identical to the ones from Poseidon.
