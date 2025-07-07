# [Cloud Run Hackathon NY](https://nyc.aitinkerers.org/p/agentic-ai-app-hackathon-with-google-cloud-run-gpus) Planning Doc

Authors: [Lisa Shen](mailto:lisashen@google.com) [Amit Maraj](mailto:amaraj@google.com)  
Collaborators: [Shir Meir Lador](mailto:slador@google.com) [Valentin Deleplace](mailto:deleplace@google.com)[James Ma](mailto:jscma@google.com)

## Objective:

- Increase GenAI developer awareness and build community around Cloud Run.
- Encourage startup adoption of Cloud Run.
- Increase awareness of Cloud Run GPUs
- Developer acquisition
- Get some interesting use cases for Cloud Run

## Requirements:

The hackathon project must focus on **building and deploying AI agents on Google Cloud Run**.

**Core Requirements:**

- **Runtime Deployment:** All **agentic AI applications** must be deployed and run on **Cloud Run**.
- **Open Model Hosting:** You _must_ leverage **Cloud Run GPUs** to host one open model for your agent's inference.
  - Please choose cost effective non-zonal redundancy option
  - Each team are expected to use **1 GPU per project** (3 GPUs per project available by default, but we only allocate onRamp credit assuming 1 GPUs)
- We also provide a clear instruction on how to quickly load Gemma3n with Ollama as an example. Amit to write a small sample of how to use it.

**Optional:**

1. **Additional LLMs:** If your agent requires capabilities beyond your hosted open model, you are welcome to **call Gemini via APIs**.
2. **Model Flexibility:** While we will provide examples (e.g., for **Gemma3** or **SDXL** on Cloud Run GPUs), you are free to host other compatible open models on Cloud Run for your inference applications.
3. [**An Agent Development Kit (ADK) example with serverless GPU is also given if you want to use it.**](https://google.github.io/adk-docs/agents/models/#using-open-local-models-via-litellm)
4. **Link to doc of MCP servers on cloud run**

## Delivery method:

1. GPU Quota is available so we should use Google Cloud project for this project.

OR:

2. Gitrepo: \- where is the code stored. Is it OSS?

2 day total with 1.5 hour presentation: Cloud Run/GPUs;

**OnRamp Credit \- need [Valentin Deleplace](mailto:deleplace@google.com)to confirm if this can support GPU**  
 “Projects using Cloud Run nvidia-l4 GPUs in a region for the first time are automatically granted 3 GPU quota (zonal redundancy off) when the first deployment is created.”. What we need to do is to assume 1 GPU is used per project, and estimate the needed credit accordingly for max 2 day during. We are not responsible for developers running out of credit if they use 3 GPUs for whatever reason.

### **Venue Location:**

Betaworks, 29 Little W 12th St, New York, NY 10014  
[https://g.co/kgs/rjPHzHd](https://g.co/kgs/rjPHzHd)

## Action items and tracking \- Lisa to convert this into a table and put owners here

| Action Items                                                                 | AI Owners                                                                      | Due Date    |                                                                                                                                                                                                        |
| :--------------------------------------------------------------------------- | :----------------------------------------------------------------------------- | :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Landing page                                                                 | [Lisa Shen](mailto:lisashen@google.com)                                        | June 24     | Done. [Page here](https://nyc.aitinkerers.org/p/agentic-ai-app-hackathon-with-google-cloud-run-gpus)                                                                                                   |
| GPU quota                                                                    | [Lisa Shen](mailto:lisashen@google.com)                                        | Jul 6, 2025 | Lisa to talk to eng team to ensure quota \- use europe region                                                                                                                                          |
| Sample Code                                                                  | [Amit Maraj](mailto:amaraj@google.com)                                         | July 6      | 1.Existing codelabs (lisa has it) 2.ADK and Cloud Run GPUs 3.Set up a project and provide sample code for ppl to call Gemma3 as an API? \- alternative option for ppl to set up its own model on GPUs? |
| What code repo for attendees                                                 | [Amit Maraj](mailto:amaraj@google.com)                                         | July 6      | Should we just ask everyone to use Git Repo                                                                                                                                                            |
| Full hackathon guideline requirement for attendees with our sample code link | [Amit Maraj](mailto:amaraj@google.com) [Lisa Shen](mailto:lisashen@google.com) | Jul 6, 2025 | See the core requirements section Lisa put at the beginning of the doc as a starting point. We will post the finished guidelines to AI Tinkerer site                                                   |
| OnRamp sign on and credit guides                                             | [Valentin Deleplace](mailto:deleplace@google.com)                              | July 6      |                                                                                                                                                                                                        |
| Judging criteria                                                             | [Lisa Shen](mailto:lisashen@google.com)                                        | July 10     |                                                                                                                                                                                                        |
| Onsite support team list                                                     | [Lisa Shen](mailto:lisashen@google.com)                                        | June 28     |                                                                                                                                                                                                        |
| Get support from Nvidia                                                      | [Lisa Shen](mailto:lisashen@google.com)                                        | June 28     | Emailed Jill. Nvidia will add this to is social media                                                                                                                                                  |
| Social media                                                                 | [Allison Park](mailto:allisonpark@google.com)                                  | Jul 1, 2025 |                                                                                                                                                                                                        |
| SWAGs                                                                        | [Allison Park](mailto:allisonpark@google.com)                                  |             |                                                                                                                                                                                                        |
| PRIZEs                                                                       | Johnathon                                                                      |             |                                                                                                                                                                                                        |

1. Valentin to collaborate on the user guidelines for using the onRamp credit (see the OnRamp testing tab)
2. Amit to provide Hackathon samples
   1. Provide some sample code for calling serverless GPUs with Gemma 3/Ollama
   2. ADK example with Cloud Run
3. Who owns the code that developers write? Do we have the right to use the code afterwards? Do they need to sign any IP release doc?
4. Amit: Gitrepo: [**https://github.com/GoogleCloudPlatform/devrel-demos**](https://github.com/GoogleCloudPlatform/devrel-demos)
5. Lisa to check with Jonathon on Internet speed for model downloading

Examples of other hackathons:

- [an example of an event with multiple sponsors, the OpenAI hackathon.](https://nyc.aitinkerers.org/p/openai-realtime-voice-x-reasoning-hackathon-ai-tinkerers)
- [https://nyc.aitinkerers.org/p/open-source-nyc-computer-vision-hackathon](https://nyc.aitinkerers.org/p/open-source-nyc-computer-vision-hackathon)
- RSVP example: [http://rsvp.withgoogle.com/events/build-with-ai-google-io](http://rsvp.withgoogle.com/events/build-with-ai-google-io) 5/19
- [Coreweave](https://semianalysis.com/hackathon-2025/?utm_content=327205203&utm_medium=social&utm_source=linkedin&hss_channel=lcp-36121341)
- AI hackathon in US ideas: [link](https://sites.google.com/corp/google.com/cloud-devrel/programs/learning-development/genai-hackathon)
- AI Hackathon in Japan:[link](https://googlecloudjapanaihackathon.devpost.com/)
- [https://cloud.google.com/blog/topics/developers-practitioners/attend-the-google-cloud-genai-roadshow](https://cloud.google.com/blog/topics/developers-practitioners/attend-the-google-cloud-genai-roadshow)
- AGI House Q2/Q3 hackathon idea:  
  [Multimodal search with](https://cloud.google.com/blog/products/ai-machine-learning/combine-text-image-power-with-vertex-ai?utm_source=linkedin&utm_medium=unpaidsoc&utm_campaign=fy25q1-googlecloud-blog-ai-in_feed-no-brand-global&utm_content=-&utm_term=-&linkId=12610621) AI studio
