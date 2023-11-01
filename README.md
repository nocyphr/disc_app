- [DISC App](#disc-app)
  - [Business Goal](#business-goal)
  - [Basic Capabilities](#basic-capabilities)
    - [1. Assessment Input:](#1-assessment-input)
    - [2. DISC Scoring System:](#2-disc-scoring-system)
    - [3. Visual Representations:](#3-visual-representations)
- [In Progress](#in-progress)
  - [Capability: questionaire](#capability-questionaire)
  - [Key feature: questionaire](#key-feature-questionaire)


# DISC App

## Business Goal
In order to hire the right person for the right job and create a great team composition
As a hiring manager 
I want to have a tool that lets me categorize their personality type according to the DISC model

Description:
The DISC model identifies four main personality traits: Dominance (D), Influence (I), Steadiness (S), and Conscientiousness (C).
 
Utilizing this model aids hiring managers in:
1. Team Balance: Ensuring diverse teams with a mix of leaders (D), communicators (I), stabilizers (S), and detail-oriented members (C).
2. Role Suitability: Aligning candidates with roles that match their inherent strengths.
3. Streamlined Training: Tailoring onboarding based on individual personality traits.
4. Conflict Minimization: Anticipating and addressing potential team conflicts through understanding of personalities.

This tool, therefore, promises better team dynamics, higher productivity, and reduced turnover by making informed hiring decisions.

## Basic Capabilities
### 1. Assessment Input:
- **Questionnaire**: Implement a DISC-based questionnaire for candidates.

### 2. DISC Scoring System:
- **Automatic Scoring**: Categorize candidates into D, I, S, or C based on responses.
- **Breakdown**: Provide a detailed distribution of each category for each individual (e.g., 50% D, 30% I, 10% S, 10% C).

### 3. Visual Representations:
- **Individual Profiles**: Use pie charts or bar graphs to show an individual's DISC distribution.

# In Progress
## Capability: questionaire  
Contributes to disc.businessgoal
To be able to ask a user a sequence of questions

## Key feature: questionaire  
Contributes to questionaire.capability

In order to get a measurable picture of the personality category of an applicant  
As a hiring manager
I want a set of questions presented in sequence to the applicant in a multiple choice format  

Description: 
    GIVEN an email
    AND a first name
    AND a last name
    AND an age
    AND a set of questions
    WHEN a user has answered all questions
    THEN I receive a set of answers that I can evaluate

