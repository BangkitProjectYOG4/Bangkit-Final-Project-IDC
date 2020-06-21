//#############################################################

// ### 1. LOAD THE TWO MODELS IMMEDIATELY WHEN THE PAGE LOADS

//#############################################################


// BREAST CANCER MODEL
// This model will load first
const MODEL_PATH = './idc_model_v1/model.json';

let breast_cancer_model;
(async function () {
	
	
	breast_cancer_model = await tf.loadLayersModel(MODEL_PATH, {});
	$("#selected-image").attr("src", "/assets/normal.png");

	$('.progress-bar').hide();

	idc_cancer_predictOnLoad();
});

//######################################################################

// ### 2. MAKE A PREDICTION ON THE FRONT PAGE IMAGE WHEN THE PAGE LOADS

//######################################################################

// After the model loads we want to make a prediction on the default image.
// Thus, the user will see predictions when the page is first loaded.

function simulateClick(tabID) {
	document.getElementById(tabID).click();
}


function idc_cancer_predictOnLoad() {

	$('.breast-cancer').hide();
	// Simulate a click on the predict button
	setTimeout(simulateClick.bind(null, 'predict-button'), 500);
}



$("#predict-button").click(async function () {
	let image = undefined;

	image = $('#selected-image').get(0);

	// Pre-process the image
	let tensor = tf.fromPixels(image)
		.resizeNearestNeighbor([50, 50]) // change the image size here
		.toFloat()
		.div(tf.scalar(255.0))
		.expandDims();


	// Pass the tensor to the model and call predict on it.
	// Predict returns a tensor.
	// data() loads the values of the output tensor and returns
	// a promise of a typed array when the computation is complete.
	// Notice the await and async keywords are used together.
	let predictions = await breast_cancer_model.predict(tensor).data();
	let top5 = Array.from(predictions)
		.map(function (p, i) { // this is Array.map
			return {
				probability: p,
				className: BREAST_CANCER_CLASSES[i]
			};


		}).sort(function (a, b) {
			return b.probability - a.probability;

		}).slice(0, 2);


	// Append the file name to the prediction list
	var file_name = 'normal.png';
	$("#prediction-list").append(`<li class="w3-text-teal">${file_name}</li>`);

	//$("#prediction-list").empty();
	top5.forEach(function (p) {

		$("#prediction-list").append(`<ol>${p.className}: ${p.probability.toFixed(6)}</ol>`);


	});


});

//#########################################################

// Code that will be executed when the user submits images.

// The code below directs the execution to either the breast_cancer_analyzer.js
// file or to the met_cancer_analyzer.js file - where the prediction is made.

//##########################################################


// This listens for a change. It fires when the user submits images.

$("#image-selector").change(async function () {
	fileList = $("#image-selector").prop('files');

	//$("#prediction-list").empty();

	// Start predictiing
	breast_processArray(fileList);
	//}
});