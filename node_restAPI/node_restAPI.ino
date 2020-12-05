#include <stdio.h>
#include <ArduinoJson.h>
#include <ESP8266WebServer.h>

#define HTTP_REST_PORT 80
#define WIFI_RETRY_DELAY 500
#define MAX_WIFI_INIT_RETRY 50


const char* wifi_ssid = "TP-LINK_CA9E68";
const char* wifi_passwd = "Mallika1959";
String inputString = "";

ESP8266WebServer http_rest_server(HTTP_REST_PORT);


/**
    Function To Initialize WiFi
*/
int init_wifi() {
  int retries = 0;

  Serial.println("Connecting to WiFi..........");

  WiFi.mode(WIFI_STA);
  WiFi.begin(wifi_ssid, wifi_passwd);
  // check the status of WiFi connection to be WL_CONNECTED
  while ((WiFi.status() != WL_CONNECTED) && (retries < MAX_WIFI_INIT_RETRY)) {
    retries++;
    delay(WIFI_RETRY_DELAY);
    Serial.print(".");
    // Dots will print to show still connecting...
  }
  return WiFi.status(); // return the WiFi connection status
}

/**
    Function Of Rest API - /tempData
    Recive data from Serail port & send to API GET request
*/
void get_time_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#A");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}

void get_vehicleSpeed_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#B");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }

  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}

void get_shiftNumber_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#C");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}
void get_engineLoad_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#D");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}
void get_totalAcceleration_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#E");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}
void get_engineRPM_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#F");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}
void get_pitch_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#G");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}
void get_lateralAcceleration_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#H");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}
void get_passengerCount_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#I");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}
void get_carLoad_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#J");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}
void get_airConditionStatus_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#K");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}
void get_windowOpening_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#L");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}
void get_radioVolume_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#M");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}
void get_rainIntensity_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#N");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}
void get_visibility_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#O");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}
void get_driverWellBeing_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#P");
  // Keep a delay untill recive the data from serial port
  delay(1000);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }
  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}

void get_driverRush_data() {
  // #T will be the request code/ the Java app will return data for #T code
  Serial.println("#Q");
  // Keep a delay untill recive the data from serial port
  delay(500);
  // Check serial port data
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, That mean finished reciving data
    if (inChar == '\n') {
      break;
      // Now lets break from this loop & send data
    }
  }


  // Create JSON object to send data
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& jsonObj = jsonBuffer.createObject();
  char JSONmessageBuffer[200];

  jsonObj["dataSet"] = inputString;
  jsonObj.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  http_rest_server.send(200, "application/json", JSONmessageBuffer);

  // Data has send, lets reset the serial data keeping string
  inputString = "";
}

/**
    config REST API function
*/
void config_rest_server_routing() {
  http_rest_server.on("/", HTTP_GET, []() {
    http_rest_server.send(200, "text/html",
                          "Welcome to the ESP8266 REST Web Server");
  });

  // Add your REST APIs & the functions to be run when call those APIs
  // http://192.168.1.7/tempdata
  http_rest_server.on("/time", HTTP_GET, get_time_data);
  http_rest_server.on("/vehicleSpeed", HTTP_GET, get_vehicleSpeed_data);
  http_rest_server.on("/shiftNumber", HTTP_GET, get_shiftNumber_data);
  http_rest_server.on("/engineLoad", HTTP_GET, get_engineLoad_data);
  http_rest_server.on("/totalAcceleration", HTTP_GET, get_totalAcceleration_data);
  http_rest_server.on("/engineRPM", HTTP_GET, get_engineRPM_data);
  http_rest_server.on("/pitch", HTTP_GET, get_pitch_data);
  http_rest_server.on("/lateralAcceleration", HTTP_GET, get_lateralAcceleration_data);
  http_rest_server.on("/passengerCount", HTTP_GET, get_passengerCount_data);
  http_rest_server.on("/carLoad", HTTP_GET, get_carLoad_data);
  http_rest_server.on("/airConditionStatus", HTTP_GET, get_airConditionStatus_data);
  http_rest_server.on("/windowOpening", HTTP_GET, get_windowOpening_data);
  http_rest_server.on("/radioVolume", HTTP_GET, get_radioVolume_data);
  http_rest_server.on("/rainIntensity", HTTP_GET, get_rainIntensity_data);
  http_rest_server.on("/visibility", HTTP_GET, get_visibility_data);
  http_rest_server.on("/driverWellBeing", HTTP_GET, get_driverWellBeing_data);
  http_rest_server.on("/driverRush", HTTP_GET, get_driverRush_data);
}

void setup(void) {
  Serial.begin(115200);
  Serial.println("MCU Program Started...");
  if (init_wifi() == WL_CONNECTED) {
    Serial.println("WIFI Connetted");
    Serial.print(wifi_ssid);
    Serial.print("--- IP: ");
    Serial.println(WiFi.localIP());
  }
  else {
    Serial.print("Error connecting to: ");
    Serial.println(wifi_ssid);
  }

  config_rest_server_routing();

  http_rest_server.begin();
  Serial.println("HTTP REST Server Started");
}

void loop(void) {
  http_rest_server.handleClient();
}
