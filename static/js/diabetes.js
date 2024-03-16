function returnToPreviousPage() {
  // window.history.back();
  location.reload();
}
// form:
function validateForm() {
  //gender
    let gender = document.forms["diabetes"]["gender"].value;
    if (Number(gender) != 1 && Number(gender) != 0) {
      alert("Error you must enter valid input in (Gender) area try again to get an accurate result");
      returnToPreviousPage();
      return false;
    }
  //age
    let age = document.forms["diabetes"]["age"].value;
    if (Number(age) <= 0 || Number(age) >= 100) {
      alert("Error you must enter valid input in (Age) area try again to get an accurate result");
      returnToPreviousPage();
      return false;
    }
  //hypertension
  let hypertension = document.forms["diabetes"]["hypertension"].value;
  if (Number(hypertension) != 1 && Number(hypertension) != 0) {
    alert("Error you must enter valid input in (Hypertension) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Heart Disease
  let heart_disease = document.forms["diabetes"]["heart_disease"].value;
  if (Number(heart_disease) != 1 && Number(heart_disease) != 0) {
    alert("Error you must enter valid input in (Heart Disease) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Smoking History
  let smoking_history = document.forms["diabetes"]["smoking_history"].value;
    if (Number(smoking_history) < 0 || Number(smoking_history) > 4) {
      alert("Error you must enter valid input in (Smoking History) area try again to get an accurate result");
      returnToPreviousPage();
      return false;
    }
  //bmi
  let bmi = document.forms["diabetes"]["bmi"].value;
  if (Number(bmi) < 10 || Number(bmi) > 95) {
    alert("Error you must enter valid input in (BMI) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //HbA1c_level
  let HbA1c_level = document.forms["diabetes"]["HbA1c_level"].value;
  if (Number(HbA1c_level) < 3.5 || Number(HbA1c_level) > 9) {
    alert("Error you must enter valid input in (Glycated Haemoglobin (HbA1c) Level) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //blood_glucose_level
  let blood_glucose_level = document.forms["diabetes"]["blood_glucose_level"].value;
  if (Number(blood_glucose_level) < 80 || Number(blood_glucose_level) > 300) {
    alert("Error you must enter valid input in (Blood Glucose Level) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  }