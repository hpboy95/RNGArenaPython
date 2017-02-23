//
//  EndGameScene.swift
//  RNG Arena
//
//  Created by Hezekiah Valdez on 12/7/16.
//  Copyright © 2016 Hezekiah Valdez. All rights reserved.
//

import Foundation
import SpriteKit

class EndGame: SKScene {
    
    //Necessary default init
    required init?(coder aDecoder: NSCoder){
        super.init(coder: aDecoder)
    }
    
    var scoreLabel = SKLabelNode(fontNamed: "AmericanTypewriter-Bold")
    var winOrLose = SKLabelNode(fontNamed: "AmericanTypewriter-Bold")
    var highscore = SKLabelNode(fontNamed: "AmericanTypewriter-Bold")
    var playAgain = SKLabelNode(fontNamed: "AmericanTypewriter-Bold")
    var quit = SKLabelNode(fontNamed: "AmericanTypewriter-Bold")
    
    override init(size: CGSize) {
        
        super.init(size: size)
        
        //Position Ids
        let xcenter = self.size.width / 2
        let ypos = (self.size.height / 7)
        
        //Score label
        scoreLabel.fontSize = 30
        scoreLabel.fontColor = SKColor.white
        scoreLabel.text = "Score: " + String(RAEngine.sharedInstance.score)
        scoreLabel.horizontalAlignmentMode = .center
        
        //Win or Lose label
        winOrLose.fontSize = 40
        winOrLose.fontColor = SKColor.white
        winOrLose.text = "You Lose"
        winOrLose.horizontalAlignmentMode = .center
        
        //Highscore label
        highscore.fontSize = 30
        highscore.fontColor = SKColor.white
        highscore.text = "Highscore: " + String(RAEngine.sharedInstance.highScore)
        highscore.horizontalAlignmentMode = .center

        //Play Again label
        playAgain.fontSize = 40
        playAgain.fontColor = SKColor.orange
        playAgain.text = "Play Again"
        playAgain.horizontalAlignmentMode = .center
        
        //Quit label
        quit.fontSize = 30
        quit.fontColor = SKColor.orange
        quit.text = "Quit"
        quit.horizontalAlignmentMode = .center
        
        scoreLabel.position = CGPoint(x: xcenter, y: ypos * 4 + 15)
        winOrLose.position = CGPoint(x: xcenter, y: ypos * 6)
        highscore.position = CGPoint(x: xcenter, y: ypos * 4 - 15)
        playAgain.position = CGPoint(x: xcenter, y: ypos * 2)
        quit.position = CGPoint(x: xcenter, y: ypos * 2 - 45)
        
        addChild(scoreLabel)
        addChild(highscore)
        addChild(winOrLose)
        addChild(playAgain)
        addChild(quit)
        
    }
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        // Loop over all the touches in this event
        for touch: AnyObject in touches {
            // Get the location of the touch in this scene
            let location = touch.location(in: self)
            
            // Check if the location of the touch is within the button's bounds
            if playAgain.contains(location){
                let transition = SKTransition.fade(withDuration: 0.5)
                let gameScene = GameScene(size: self.size)
                self.view?.presentScene(gameScene, transition: transition)
            }
            if quit.contains(location){
                self.view?.removeFromSuperview()
            }
        }
        
    }

    
}
