package controllers

import (
	"net/http"

	"github.com/usefss/cab-please/identity/auth"
	"github.com/usefss/cab-please/identity/models"
	"github.com/usefss/cab-please/identity/permission"

	"github.com/gin-gonic/gin"
)

type UserSignupInput struct {
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
	IsAdmin  bool   `json:"is_admin"`
}

type UserLogin struct {
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
}

// ObtainJWT godoc
// @Summary   Obtain JWT
// @Accept   json
// @Param user body UserLogin true "User Data"
// @Success 200 {object} object
// @Produce  json
// @tags 	  User
// @Router   /api/users/login [post]
func ObtainJWT(c *gin.Context) {
	var input UserLogin
	if err := c.ShouldBindJSON(&input); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	var user models.User
	if err := models.DB.Where("username = ?", input.Username).First(&user).Error; err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "User not found!"})
		return
	}
	if !models.VerifyPassword(user.Password, input.Password) {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Wrong password!"})
		return
	}
	token := auth.CreateJWT(user.ID, user.Username, user.IsAdmin)
	c.JSON(http.StatusOK, gin.H{"access": token})
}

// SignupUser godoc
// @Summary   Signup user
// @tags 	  User
// @Param user body UserSignupInput true "User Data"
// @Success 200 {object} object
// @Accept    json
// @Produce   json
// @Router    /api/users/signup [post]
func SignupUser(c *gin.Context) {
	var input UserSignupInput
	if err := c.ShouldBindJSON(&input); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	user := models.User{
		Username: input.Username,
		Password: models.HashPassword(input.Password),
		IsAdmin:  input.IsAdmin,
	}
	result := models.DB.Create(&user)
	if result.Error == nil {
		c.JSON(http.StatusOK, gin.H{"user": user})
	} else {
		c.JSON(http.StatusBadRequest, gin.H{"error": result.Error})
	}
}

// GetProfile godoc
// @Summary   get user profile
// @Accept   json
// @Produce  json
// @tags 	  User
// @Success 200 {object} object
// @Security ApiKeyAuth
// @Router   /api/users/profile [get]
func GetProfile(c *gin.Context) {
	user, isAuthorized := permission.IsAuthenticated(c)
	if !isAuthorized {
		c.JSON(http.StatusForbidden, gin.H{"error": "You are not authorized to access!"})
		return
	}
	c.JSON(http.StatusOK, gin.H{
		"id":       (*user).ID,
		"username": (*user).Username,
	})
}
