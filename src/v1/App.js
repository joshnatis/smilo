import React from 'react';
import { Image, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import person from './assets/pics/img3.jpg';
import smilo from './assets/icon.png';
import { Audio } from 'expo-av';

export default function App() {
  return (
    <View style={styles.container} onLoad={playSound()}>
     <Image source={smilo} style={styles.logo}></Image>
      <Text style={styles.question}> What emotion is this person feeling?</Text>
      <Image source={person} style={styles.person}/>

     <View style={styles.button_row}>
       <TouchableOpacity
          onPress={() => alert('Happy')}
          style={styles.button}>
          <Text style={styles.buttonText}>Happy</Text>
        </TouchableOpacity>

       <TouchableOpacity
          onPress={() => alert('Sad.')}
          style={styles.button}>
          <Text style={styles.buttonText}>Sad</Text>
        </TouchableOpacity>

       <TouchableOpacity
          onPress={() => alert('Surprised.')}
          style={styles.button}>
          <Text style={styles.buttonText}>Surprised</Text>
        </TouchableOpacity>
      </View>
    </View>
  );

}


async function playSound() {
  const soundObject = new Audio.Sound();
  try {
    await soundObject.loadAsync(require('./assets/buusound.wav'));
    await soundObject.playAsync();
  }
  catch (error) {
    alert("Sound was not loaded!");
  }

}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },

  button_row: {
    marginTop: 30,
    flexDirection: 'row',
    justifyContent: 'space-between',
  },

  person: {
    width: 305,
    height: 260,
    borderRadius: 10,
    borderWidth: 2,
    borderColor: '#888',
    marginBottom: 10,
    marginTop: 30,
  },

  question: {
    color: '#888',
    fontSize: 20,
    marginHorizontal: 15,
  },

  button: {
    backgroundColor: '#a9cbfc',
    padding: 20,
    borderRadius: 100,
    marginHorizontal: 5,
    borderColor: '#888',
    borderWidth: 1,
  },

  buttonText: {
    fontSize: 20,
    color: '#fff',
  },

  logo: {
    marginTop: -70,
    marginBottom: 10,
    width: 100,
    height: 100,
  }
});
